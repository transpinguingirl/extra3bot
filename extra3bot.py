import tweepy
import datetime
import xml.etree.ElementTree as ET
import urllib.request
import locale
import os
locale.setlocale(locale.LC_TIME, "de_DE")
HP = urllib.request.urlopen('http://www.ndr.de/fernsehen/sendungen/extra_3/index.html')
v = HP.read()
#from html.parser import HTMLParser
# create a subclass and override the handler methods
#class MyHTMLParser(HTMLParser):
 #      def handle_starttag(self, tag, attrs):
  #            print( "Encountered a start tag:", attrs)
   #    def handle_endtag(self, tag):
    #          print( "Encountered an end tag :", tag)
     #  def handle_data(self, data):
      #        print( "Encountered some data  :", data)

# instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
#parser.feed(v.decode("utf-8") )
auth = tweepy.OAuthHandler("key", "key")
auth.set_access_token("key", "key")

api = tweepy.API(auth)

from bs4 import BeautifulSoup
soup = BeautifulSoup(v, 'html.parser')
#print(soup.prettify())
for div in soup.find_all("div"):
    #print(div.get('class'))
    if div.get('class') == ['module', 'box', 'w100', 'list']:
        #print(div.get('class'))
        for sdiv in div.find_all("div"):
            #print(sdiv.get('class'))
            if sdiv.get('class') == ["teaserpadding"]:
                datum = sdiv.find("h2").string
                if "Wiederholungen der Sendung" in datum.string:
                    continue
                datum = datum.split(" Uhr im ")
                #print(datum[0])
                #print(datum[0][4:])
                datum[0] = datetime.datetime.strptime(datum[0][5:], '%d.%m.%Y | %H:%M')
                #print(datum[1])
                #Mi, 30.08.2017 | 22:50 Uhr im NDR extra 3 Spezial - Der reale Irrsinn XXL
                #Do, 31.08.2017 | 22:45 Uhr im Ersten
                if datum[0].strftime("%d.%m.%Y") == datetime.date.today().strftime("%d.%m.%Y"):
                    if "extra 3 Spezial" in datum[1]:
                        if "Uhr im Ersten" in datum[1]:
                            api.update_status("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 " + datum[1].split("extra 3 ")[1] + " im @DasErste")
                            break
                        else:
                            api.update_status("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 " + datum[1].split("extra 3 ")[1] + " im @" + datum[1].split(" extra 3")[0])
                            print ("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 " + datum[1].split("extra 3 ")[1] + " im @" + datum[1].split(" extra 3")[0])
                            break
                    else:
                        if "Uhr im Ersten" in datum[1]:
                            api.update_status("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 im @DasErste")
                            break
                        else:
                            api.update_status("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 im @" + datum[1])
                            #print ("Heute Um " + datum[0].strftime("%H:%M") + "\n läuft @extra3 im @" + datum[1])
                            break
                else:
                    if datetime.date.today().strftime("%A") == "Montag":
                        if "extra 3 Spezial" in datum[1]:
                            if "Uhr im Ersten" in datum[1]:
                                api.update_status(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3" + datum[1].split("extra 3 ")[1] + " im @DasErste")
                                #print(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3" + datum[1].split("extra 3 ")[1] + " im @DasErste")
                                break
                            else:
                                api.update_status(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3" + datum[1].split("extra 3 ")[1] + " im @" + datum[1].split(" extra 3")[0])
                                #print(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3" + datum[1].split("extra 3 ")[1] + " im @" + datum[1].split(" extra 3")[0])
                                break
                        else:
                            if "Uhr im Ersten" in datum[1]:
                                api.update_status(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3 im @DasErste")
                                #print(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3 im @DasErste")
                                break
                            else:
                                api.update_status(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3 im @" + datum[1])
                                #print(" Am " + datum[0].strftime("%A den %d.%m.%Y um %H:%M ") + "läuft @extra3 im @" + datum[1])
                                break
