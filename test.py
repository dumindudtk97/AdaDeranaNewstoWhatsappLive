from twilio.rest import Client 
from bs4 import BeautifulSoup
import requests
#import pywhatkit
from datetime import datetime


account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 

def scrape():
    print("starting...")
    # get news page
    url_to_scrape = "http://www.adaderana.lk/hot-news/"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    r = requests.get(url_to_scrape,headers=headers)
    print(r.status_code)


    # get html parser
    html_soup = BeautifulSoup(r.text, 'html.parser')


    # get news story sections
    hotNewsStories = html_soup.find_all('div',class_="news-story")
    #print(hotNewsStories)

    # open csv file to write
    filename = 'hotNewsStories.csv'
    f = open(filename,'r+')
    # add headers to csv file
    headerlines = 'Headline,Date&Time,story,url\n'
    f.write(headerlines)


    # scrape information
    for News in hotNewsStories:
    
        story = News.find('div',class_="story-text")  # contain full news story
    
        toURL = story.find_next('a')              # url and headline a tag
        url = format(toURL.get("href"))

        Headline = story.find_next('a').text      # a tag text (headline)
        Headline = Headline.replace(',',' ')

        abstract = story.find_next('p').text      # p tag contain abstract of the story
        abstract = abstract.replace(' MORE..','')
        abstract = abstract.replace(',',' ')

        dateTime = story.find_next('div',class_="comments pull-right")
        dateTime = dateTime.find_next('span').text
        dateTime = dateTime.replace('| ','')
        dateTime = dateTime.replace(',','')
        dateTime = dateTime.replace('&nbsp;&nbsp;','')
        print('\n')
        #print(abstract)
        #print(Headline)
        print(url)
        check = url
        #print(dateTime)
        print('\n')
        infile = False  # assume url is not in file
             
        f.seek(0)
        for line in f.readlines():
            if check in line:
                infile = True               # if url is in file -->  infile = False
                print("url is in file")
                break
            else:
                infile = False
        print(infile)
        try:
            if infile == False :        # do if not in in file
                f.write(Headline+ ','+ dateTime + ','+ abstract+ ','+url + ',\n')
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                x = current_time.split(":")
                #pywhatkit.sendwhatmsg_instantly("+94711870149",url,10,True)
                msg = url + '\n' + abstract + '\n' + dateTime
                #
                # pywhatkit.sendwhatmsg_to_group("JWCEMexf39q2Mgmj02VwVy",url,int(x[0]),int(x[1])+1,25,True,True)
                print("Successfully Sent!")
                send_msg(msg)
            else:
                print("url in list")
                print(check)
            
        except:


            print("exception occured")
            #ignore write exception (only a \x9x char problem) 
        
        
        


def send_msg(msg):
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=msg,      
                              to='whatsapp:+94711870149' 
                          ) 
 
    print(message.sid)

scrape()
