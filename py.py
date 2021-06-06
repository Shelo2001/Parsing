from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint
file=open('books.csv','w')
file.write('Title,Author,Price')
file_obj=csv.writer(file)
file_obj.writerow(['Title','Author','Price'])
ind=1
while ind <=5:
    url='https://www.lit.ge/index.php?page=audios&send[shop.catalog][page]=0'+str(ind)
    r=requests.get(url)
    content=r.text
    soup=BeautifulSoup(content, 'html.parser')
    all_books=soup.find('section',class_='list-holder')
    books_list=all_books.find_all('div',class_='span10')
    ind+=1
    for each in books_list:
        title=each.a.text
        print(title)
        author=each.span.b.a.text
        print(author)
        price=each.button.text
        print(price)
        # file_obj.writerow([title, author, price])
        # file.write(title+','+author+','+price+'\n')
    sleep(randint(15,20))
