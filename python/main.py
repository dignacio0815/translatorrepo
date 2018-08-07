import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
'''
    
num1 = raw_input("Type in your number: ")
num2 = raw_input("Type in your number: ")
sum = int(num1) + int(num2) 
print "Sum: " + str(sum)
num = 1
if num > 0: 
    print("Positive")
   
elif num < 0:
    print("Negative")
else:
    print("Neither")

for i in range(5):
    print(i)
    
string = "hello there!"
for letter in string:
    print(letter)

string = "Strawberry Fields"
i = 0
while i < len(string):
    print string
    i = i + 1  
   ''' 
    


    
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template(' ')
        self.response.write(about_template.render())


class SpanishPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('../html/spanish.html ')
        self.response.write(about_template.render())
        
    def post(self): 
        html = the_jinja_env.get_template('html/spanish.html')
        

class JapanesePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/japanese.html ')
        self.response.write(about_template.render())
         
    def post(self): 
        html = the_jinja_env.get_template('html/japanese.html')

class VietnamesePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/vietnamese.html')
        self.response.write(about_template.render())
    
    def post(self): 
        html = the_jinja_env.get_template('html/vietnamese.html')

class TagalogPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/tagalog.html ')
        self.response.write(about_template.render())
        
def post(self): 
        html = the_jinja_env.get_template('html/tagalog.html')

class EnglishPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/english.html')
        self.response.write(about_template.render())
    def post(self): 
        html = the_jinja_env.get_template('html/english.html')
'''
    def post(self):
        if (i == 1):
            self.response.write("/spanish")
        elif (i == 2):
            self.response.write("/japanese")
        elif (i == 3):
            self.response.write("/vietnamese")
        elif (i == 4):
            self.response.write("/tagalog")
        else:
            self.response.write("/english")
            '''         
app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/spanishmood', SpanishPage),
], debug=True)
