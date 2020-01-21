import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://www.ppomppu.co.kr/hot.php'
PPOMPPU = 'http://www.ppomppu.co.kr/'

def extract_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    page_list= soup.find('td',{'id':'page_list'})
    page_list_links = page_list.find_all('a')

    pages = []

    for link in page_list_links[:-1]:
        pages.append(int(link.string))

    return max(pages)   
    

def extract_page_write(max_pages):

    writing_list = []
    
    for page in range(max_pages):

        result = requests.get(f'{URL}?i&page={page+1}')        
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('td',{'align' : 'left'})
        writing_list.append(['URL','TITLE'])

        for i in results: 
            x = i.find('a')

            if x is not None:
                site = 'http://www.ppomppu.co.kr'+ str(x.get('href'))
                text = x.text
                writing_list.append([text,site])
        
    return writing_list 

def save_to_file(ppomppu):
    file = open('ppomppu.csv','w', encoding='utf-8', newline='')
    writer = csv.writer(file)
    for i in ppomppu:
        writer.writerow(i)
    file.close()
    

x = extract_page()
y = extract_page_write(x)
save_to_file(y)
