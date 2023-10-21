from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

print(doc.select('.heading-60-black.color-black.mb-20'))

courses = doc.select('.heading-60-black.color-black.mb-20')

[<h2 class="heading-60-black color-black mb-20">
                    Choose Your Course                </h2>, <h2 class="heading-60-black color-black mb-20">
                            Software Engineering                        </h2>, <h2 class="heading-60-black color-black mb-20">
                            Data Science                        </h2>, <h2 class="heading-60-black color-black mb-20">
                            Product Design                        </h2>, <h2 class="heading-60-black color-black mb-20">
                            Cybersecurity Engineering                        </h2>]

                            
for course in courses: 
  print(course.contents[0].strip())