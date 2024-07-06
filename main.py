from bs4 import BeautifulSoup
courses_dict = {}
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all('div', class_='card')
    for course in courses_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        courses_dict[course_name] = int(course_price[:-1:])
        print(f'{course_name} costs {course_price}')
        print(courses_dict)
