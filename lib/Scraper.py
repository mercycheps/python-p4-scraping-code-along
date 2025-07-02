from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:
    def __init__(self):
     self.courses = []
     
    def get_page(self):
      doc =  BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')
      return doc
  
    def make_courses(self):
        for course in self.get_courses():

            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses
    
    def get_courses(self):
      doc = self.get_page()
      return doc.select(".post")

    def print_courses(self):
        for course in self.make_courses():
            print(course)
    #   for course in doc.select('.post'):
    #         print(type(course))

    #         title = course.select("h2")[0].text if course.select("h2") else ''
    #         date = course.select(".date")[0].text if course.select(".date") else ''
    #         description = course.select("p")[0].text  if course.select("p") else ''

    #         new_course = Course(title, date, description)
    #         self.courses.append(new_course)
