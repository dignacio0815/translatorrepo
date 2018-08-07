import webapp2
from random import shuffle
import jinja2
import os

# Imports the Google Cloud client library
from google.cloud import translate

#libraries for APIs
from google.appengine.api import urlfetch
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AboutPage(webapp2.RequestHandler):
    def get(self):
        html_template = the_jinja_env.get_template('html/intro.html')
        self.response.write(html_template.render()) 

class SpanishMoodPage(webapp2.RequestHandler):
    def post(self):
        spanish_template = the_jinja_env.get_template('spanish_mood/spanishmood.html')
        mood = self.request.get('mood')
        mood_dict = {
            "mood" : mood
        }
        self.response.write(spanish_template.render(mood_dict)) 
       
    def get(self):
        self.response.write("query executed")
        # Instantiates a client
        translate_client = translate.Client()
        # The text to translate
        text = u'Hello, world!'
        # The target language
        target = 'ru'
        # Translates some text into Russian
        translation = translate_client.translate(
            text,
            target_language=target)
        self.response.write(u'Text: {}'.format(text))
        self.response.write(u'Translation: {}'.format(translation['translatedText']))

'''        
class SpanishPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/spanish.html')
        
    def post(self): 
        html = the_jinja_env.get_template('templates/spanish.html')
'''

app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/spanishmood', SpanishMoodPage)
], debug=True)
