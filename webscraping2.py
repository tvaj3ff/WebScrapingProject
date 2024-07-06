from bs4 import BeautifulSoup
import requests


def get_python_jobs_from_hh() -> None:
    url = ('https://spb.hh.ru/search/vacancy?text=Python&from=suggest_post&area=2&hhtmFrom=main&hhtm'
           'FromLabel=vacancy_search_line')
    header = {"user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.103 Safari/537.36'}

    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, 'lxml')
    jobs = soup.find_all('div', class_='vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter')

    with open('output_files/jobs.txt', 'w') as f:
        for index, job in enumerate(jobs):
            job_name = job.find('span', class_='vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link').text
            company_name = job.find('span', class_='company-info-text--vgvZouLtf8jwBmaD1xgp').text
            experience = job.find('span', class_="label--rWRLMsbliNlu_OMkM_D3 "
                                                 "label_light-gray--naceJW1Byb6XTGCkZtUM").text
            link = job.h2.span.a['href']
            line: str = '-'*10 + str(index + 1) + '-'*10
            f.write(f'\n {line} \n')
            f.write(f'Jobs name: {job_name}\n')
            f.write(f'Company name: {company_name}\n')
            f.write(f'Experience: {experience}\n')
            f.write(f'More info link: {link}\n')

    print('Scraping Operation Completed!')


if __name__ == '__main__':
    get_python_jobs_from_hh()

