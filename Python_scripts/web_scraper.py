from requests_html import HTMLSession
import os

files = os.listdir("Articles/") #Get a list of articles present in the directory, to avoid new files overwriting old files

cnt = len(files)+1

for i in range(195,501):

    session1 = HTMLSession() #Creation of the HTMLSession

    url = 'https://www.espncricinfo.com/cricket-news?page='+str(i) #The URL from which data is to be scraped

    page = session1.get(url)
    
    print(page) #Getting Connection status, Code 200 indicates "OK"

    page.html.render(timeout=15) 

    article_list = page.html.find('.ds-border-b.ds-border-line.ds-p-4') #Finding html elements based on this class, which includes the link of the article

    articles = [i.find("a") for i in article_list]

    articles = [i for sublist in articles for i in sublist] #Flattening the list of articles

    for article in articles:

        session2 = HTMLSession()

        article_link = "https://espncricinfo.com"+article.attrs['href'] #Performing web scraping for each article

        if('espncricinfo' not in str(article_link)):
            continue

        article_page = session2.get(article_link)

        article_page.html.render(timeout=10)

        content_title = article_page.html.find('h1')

        article_content = content_title[0].text + "\n\n" #Getting the Title of the Article

        content = article_page.html.find('.ds-text-comfortable-m.ds-my-4.ci-html-content') #Getting the content of the article, as all the 'p' tags share the same class

        for paragraph in content:

            article_content += paragraph.text

        file_name = "Articles\\article"+str(cnt)+'.txt'

        try:
            with open(file_name,"w+",encoding='utf-8') as file:

                file.writelines(article_content) #Adding the content of each article to a file
        
        except:
                print("An Unknown error occurred while writing data into the file")

        cnt+=1

        session2.close()
    
    session1.close() #Closing both sessions