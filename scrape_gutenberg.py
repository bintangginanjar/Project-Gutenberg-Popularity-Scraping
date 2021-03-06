from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime

import pandas as pd

firefoxOptions = Options()
firefoxOptions.add_argument('-headless')

# make sure you set webDriverPath to the path where you put a geckodriver
webDriverPath = '/opt/firefox/geckodriver/geckodriver'

browser = webdriver.Firefox(executable_path=webDriverPath, options=firefoxOptions)
browser.get('http://www.gutenberg.org/ebooks/search/?sort_order=downloads')

print('Title: %s' % browser.title)

i = 1
res = {}
nameList = []
authorList = []
numOfDownloadList = []

while True:

    books = browser.find_elements_by_class_name('booklink')

    for book in books:
        try:
            name = book.find_elements_by_class_name('title')[0].text
            try:
                author = book.find_elements_by_class_name('subtitle')[0].text
            except:
                author: 'Not available'

            try:
                numOfDownload = book.find_elements_by_class_name('extra')[0].text
            except:
                numOfDownload: 'Not available'

            print('------------')
            print('Number: ', i)
            print('Name: ', name)
            print('Author: ', author)
            print('Download: ', numOfDownload)

            nameList.append(name)
            authorList.append(author)
            numOfDownloadList.append(numOfDownload)
            #res[i] = [name, author, numOfDownload]
        except:
            pass

        i = i + 1

    navButton = browser.find_elements_by_class_name('statusline')[0].find_elements_by_tag_name('a')

    if len(navButton) == 2:
        break
    else:
        navButton[-1].click()

    # print(len(navButton))

browser.quit()

res['bookName'] = nameList
res['bookAuthor'] = authorList
res['download'] = numOfDownloadList

df = pd.DataFrame(res)
# print(df)
df.to_csv('gutenberg_most_popular_book.csv')

# uploaded to github
