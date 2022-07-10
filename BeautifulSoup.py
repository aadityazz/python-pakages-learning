from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Creating a HTML content file
html = '<!DOCTYPE html>\
<html>\
<head>\
<title> Testing Web Page </title>\
</head>\
<body>\
<h1> Web Scraping </h1>\
<p id = "first_para">\
Let\'s start learning \
<b>\
Web Scraping\
</b>\
</p>\
<p class = "abc" id = "second_para">\
You can read more about BeautifulSoup from <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"> here </a>\
</p>\
<p class = "abc">\
<a href = "https://codingninjas.in/"> Coding Ninjas </a>\
</p>\
</body>\
</html>'

# Parsing the HTML file to variable data
data = BeautifulSoup(html, 'html.parser')

# Printing the html File
data

# Type of data parsed
type(data)

# To print the html in readable way we use
print(data.prettify())

# Extracting title tag
data.title

# Extracting head tag
data.head

# Extracting h1 tag
data.h1

# Extracting p tag
# Here we will get first coming p tag details
data.p

# Extracting h2 tag
# Here h2 tag isn't present in the HTML file, so it won't show anything
data.h2

# Printing the tag name
print(data.title.name)

# Printing the tag's containing string
print(data.title.string)

# Printing the tag's containing attributes
# Here we will get the empty array as we don't have any attributes in title tag
print(data.title.attrs)

# Printing the tag's containing attributes
data.p.attrs

# To get the value of id
data.p['id']

# Another way to get the value of id
data.p.get('id')

# To get the all text in the HTML webpage from any kind of tags
data.get_text()

# To find the parameter[tag]'s data
# It will print first occurring element
data.find('p')
data.find('pr')
data.find('h1')

# To get all the data of particular tags
li = data.find_all('p')

# Another way to get all the data from a particular tag in the iteration fashion
for i in li:
    print(i)

# To get all the data from multiple tags
data.find_all(['p', 'a'])

# To get all the data from every tags
data.find_all(True)

# To get all the data having id with some values
data.find_all(id='first_para')

# To get all the data having class with some values
data.find_all(class_='abc')

# Storing all the data for p tags in li
li = data.find_all('p')

# Printing all the string from li data
for i in li:
    print(i.string)

# Printing in list formal of all the string from li data
for i in li:
    print(list(i.strings))

# Printing in list formal of all the string from li data in pretty way
for i in li:
    print(list(i.stripped_strings))

# To get each and every child of a tag
li = data.html.contents
print(len(li))
print(li)

# Another way to get each and every child of a tag
# This method will produce the iterator
li_22 = data.html.children
for i in li_22:
    print(i)

# To get descendants in html file
desc = list(data.html.descendants)
print(len(desc))
desc

'''
We have few more function to parse the html tree, that are
1. Going up -> .parent, .parents
2. Going Sideways -> • next_sibling and .previous_sibling
                     • .next_siblings and .previous_siblings
3. Going Back & Forth -> • .next_element and .previous_element
                         • .next_elements and .previous_elements
                         
Will try later...
'''

'-------------------------------------------------------------------'

# Now we will start using actual webpage instead of dummy webpage

'''
Few process we need to keep in our mind is 
1. Load the HTML -> TO load the html file we need to make a get request and that 
will be done by a package known as request
2. Parse the HTML -> parsing HTML is simply done by BeautifulSoup Library
3. Operations we need to do
'''

# Send get request using the URL and accessing the HTML content
response = requests.get('http://books.toscrape.com/')
response

response.headers
html_data = response.text

data = BeautifulSoup(html_data, 'html.parser')
print(data.prettify())

data.title

data.title.string

data.a

data.a.string

data.header.a

data.header.a.string

b1 = data.find(class_='product_pod')
b1

b1.h3

b1.h3.a

b1.h3.a['title']

print('http://books.toscrape.com/' + b1.h3.a['href'])

books = data.find_all(class_='product_pod')
print(len(books))

books

base_url = 'http://books.toscrape.com/'
books_urls = []
for i in books:
    books_urls.append(base_url + i.h3.a['href'])

books_urls

'-----------------------------------------------------------------'

# Scraping a book

response = requests.get('http://books.toscrape.com/')
response

data = BeautifulSoup(response.text, 'html.parser')

# Print Link for all books
all_books = data.find_all(class_='product_pod')
print(len(all_books))

base_url = 'http://books.toscrape.com/'
urls = []
for i in all_books:
    urls.append(base_url + i.a['href'])

all_urls = ['http://books.toscrape.com/catalogue/page-1.html']
current_page = 'http://books.toscrape.com/catalogue/page-1.html'

base_url = 'http://books.toscrape.com/catalogue/'

response = requests.get(current_page)

while response.status_code == 200:
    data = BeautifulSoup(response.text, 'html.parser')
    next_page = data.find(class_='next')
    if next_page is None:
        break
    next_page_url = base_url + next_page.a['href']
    print(next_page_url)
    all_urls.append(next_page_url)

    current_page = next_page_url
    response = requests.get(current_page)

'--------------------------------------------------------------------'

# Saving the scraped data to csv file

response = requests.get('http://books.toscrape.com/')
data = BeautifulSoup(response.text, 'html.parser')
data

b1 = data.find(class_='product_pod')
b1

base_url = 'http://books.toscrape.com/'
b1_url = base_url + b1.h3.a['href']
print(b1_url)

response = requests.get(b1_url)
data = BeautifulSoup(response.text, 'html.parser')
data

title = data.h1.string
price = data.find(class_='price_color').string
qty = data.find(class_='instock availability')
qty = qty.contents[-1].strip()

print(title)
print(b1_url)
print(price)
print(qty)

qty = int(re.search('\d+', qty).group())
price = float(re.search('[\d.]+', price).group())
print(type(price))

print(title)
print(b1_url)
print(price)
print(qty)

book_details = []
book_details.append([title, b1_url, price, qty])
book_details.append([title, b1_url, price, qty])
book_details

df = pd.DataFrame(book_details, columns=['Title', 'Link', 'Price', 'Quantity in Stock'])
df

df.to_csv('books.csv', index=False)
