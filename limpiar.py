from bs4 import BeautifulSoup
import requests
import pandas as pd

# How To Get The HTML
website = 'https://chat.whatsapp.com/invite/4dWtZ4Fa0CaAbVFiZKXioQ'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# Locate the box that contains title and transcript
box = soup.find('div', class_='_9vd6 _9t33 _9bir _9bj3 _9bhj _9v12 _9tau _9tay _9u6w _9se- _9u5y')
# Locate title and transcript
title = box.find('h3').get_text()
print(title)


#transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#print(transcript)
# export data in a text file with the "title" name.
#with open(f'{title}.txt', 'w') as file:
#    file.write(title +'\n')
#    file.write(transcript)