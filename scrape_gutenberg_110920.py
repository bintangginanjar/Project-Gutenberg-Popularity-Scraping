from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

firefoxOptions = Options()
firefoxOptions.add_argument('-headless')

browser = webdriver.Firefox(executable_path='/opt/firefox/geckodriver/geckodriver', options=firefoxOptions)
browser.get('http://www.gutenberg.org/ebooks/search/?sort_order=downloads')

print('Title: %s' % browser.title)

i = 1

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
		except:
			pass

		i = i + 1

	navButton = browser.find_elements_by_class_name('statusline')[0].find_elements_by_tag_name('a')

	if len(navButton) == 2:
		break
	else:
		navButton[-1].click()

	#print(len(navButton))

browser.quit()