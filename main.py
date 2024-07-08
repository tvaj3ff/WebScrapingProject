

from bs4 import BeautifulSoup
import requests

def get_python_jobs_from_hh() -> None:
    JOB_POSITION = ""
    base_url = 'https://spb.hh.ru'
    url = f'{base_url}/vacancies/{JOB_POSITION}'
    header = {
        "user-agent": ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/51.0.2704.103 Safari/537.36')
    }
    page_number = 0

    while True:
        response = requests.get(f'{url}?page={page_number}', headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all('div', class_='vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter')

        if not jobs:
            break  # Exit loop if no jobs found (end of pages)

        for index, job in enumerate(jobs):
            job_name_tag = job.find('span', class_='vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link')
            company_name_tag = job.find('span', class_='company-info-text--vgvZouLtf8jwBmaD1xgp')
            experience_tag = job.find('span',
                                      class_="label--rWRLMsbliNlu_OMkM_D3 label_light-gray--naceJW1Byb6XTGCkZtUM")
            link_tag = job.h2.span.a if job.h2 and job.h2.span and job.h2.span.a else None

            job_name = job_name_tag.text if job_name_tag else 'N/A'
            company_name = company_name_tag.text if company_name_tag else 'N/A'
            experience = experience_tag.text if experience_tag else 'N/A'
            link = base_url + link_tag['href'] if link_tag else 'N/A'

            line = '-' * 10 + str(index + 2) + '-' * 10
            print(f'\n {line} \n')
            print(f'Job name: {job_name}\n')
            print(f'Company name: {company_name}\n')
            print(f'Experience: {experience}\n')
            print(f'More info link: {link}\n')

        page_number += 1  # Move to the next page

    print('Scraping Operation Completed!')


if __name__ == '__main__':
    get_python_jobs_from_hh()
