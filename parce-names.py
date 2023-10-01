import requests
from bs4 import BeautifulSoup

url = 'https://www.ssa.gov/oact/babynames/decades/century.html' 
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

# name_elements = soup.find_all('td')

# names_list = name_elements[2].get_text(strip=True)

# # names_list = [element.text for element in name_elements]

# with open('names2.txt', 'a', encoding='utf-8') as file:
#     for name in names_list:
#         print(name)
#         file.write(name + '\n')

rows = soup.find_all('tr')

with open('m_names.txt', 'w') as file:
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            second_element = cols[1].text.strip()
            file.write(f'{second_element}\n')