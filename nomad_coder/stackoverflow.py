import requests
from bs4 import BeautifulSoup

URL = f'http://stackoverflow.com/jobs?q=python&sort=i'

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div',{'class':'s-pagination'}).find_all('a')
    last_pages = pages[-2].get_text(strip = True)
    return int(last_pages)

def extract_jobs_plus(html):
    title =  html.find('h2').get_text(strip=True)   
    company = html.find("h3").find("span").get_text(strip=True)
    location = html.find("h3").find("span", {"class": "fc-black-500"}).get_text(strip=True)
    jobs_id = html['data-jobid']
    return {
        'title' : title,
        'company' : company,
        'location' : location,
        'apply link' : f'http://stackoverflow.com/jobs/{jobs_id}'
        }

def extract_jobs(last_page):
    jobs = []
    for page in range(1,last_page):
        result = requests.get(f'{URL}&pg={page}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div',{'class':'-job'})
        for result  in results:
           job = extract_jobs_plus(result)
           jobs.append(job)
    
    return jobs
        

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    print(jobs)
    return jobs  

    
