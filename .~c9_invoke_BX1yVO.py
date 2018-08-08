import webapp2
from random import shuffle
import jinja2
import os
from google.appengine.ext import vendor
#from google.cloud import translate

# Imports the Google Cloud client library
#from google.cloud import translate

#libraries for APIs
from google.appengine.api import urlfetch
import json

# Instantiates a client
#translate_client = translate.Client()

# The text to translate
moods = {
    "happyDict" : {
        "title":"Welcome to the translate app",
        "phraseOne": "Phrase One",
        "phraseOneTrans": "hello",
        "phraseTwo": "Phrase Two",
        "phraseTwoTrans": "bye"
        },
            "english":"how are you?", 
    "sadDict" : {
        "title":"Welcome to the translate app",
        "phraseOne": "Phrase One",
        "phraseOneTrans": "hello",
        "phraseTwo": "Phrase Two",
        "phraseTwoTrans": "bye"
    },
        
    "angryDict" :{
            "title":"Welcome to the translate app",
            "phraseOne": "Phrase One",
            "phraseOneTrans": "hello",
            "phraseTwo": "Phrase Two",
            "phraseTwoTrans": "bye"
        },
        
    "neutralDict" :{
            "title":"Welcome to the translate app",
            "phraseOne": "Phrase One",
            "phraseOneTrans": "hello",
            "phraseTwo": "Phrase Two",
            "phraseTwoTrans": "bye"
        },
        
    "quirkyDict" : {
            "title":"Welcome to the translate app",
            "phraseOne": "Phrase One",
            "phraseOneTrans": "hello",
            "phraseTwo": "Phrase Two",
            "phraseTwoTrans": "bye"
        },
}
'''
the_variable_dict = {
    "moods" : moods
}
'''
# The target language

text = 'How are you?'
target = 'jp'
        
        
#translation = translate_client.translate(
 #   text,
  #  target_language=target)


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
if os.path.isdir(os.path.join(os.getcwd(), 'lib')):
    vendor.add('lib')
    
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

class SpanishPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/spanish.html')
        self.response.write(about_template.render()) 
    
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(moods['happyDict'])) 
            # do this
            # 
        elif moodType == 'sad':
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(sadDict)) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(angryDict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(neutralDict)) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(quirkyDict)) 
        
            
        
        
        # html = the_jinja_env.get_template('html/spanish.html')
    
    
class JapanesePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/japanese.html')
        self.response.write(about_template.render())
        
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(moods['happyDict'])) 
            # do this
            # 
        elif moodType == 'sad':
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(sadDict)) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(angryDict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(neutralDict)) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(quirkyDict)) 
        
        
class VietnamesePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/vietnamese.html')
        self.response.write(about_template.render())
        
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(moods['happyDict'])) 
            # do this
            # 
        elif moodType == 'sad':
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(sadDict)) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(angryDict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(neutralDict)) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(quirkyDict))
            
        
class TagalogPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/tagalog.html')
        self.response.write(about_template.render())
    
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(moods['happyDict'])) 
            # do this
            # 
        elif moodType == 'sad':
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(sadDict)) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(angryDict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(neutralDict)) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(quirkyDict))
            
    
class EnglishPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/english.html')
        self.response.write(about_template.render())
    
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(moods['happyDict'])) 
            # do this
            # 
        elif moodType == 'sad':
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(sadDict)) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(angryDict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(neutralDict)) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(quirkyDict))
        

#print(u'Text: {}'.format(text))
#print(u'Translation: {}'.format(translation['translatedText']))
    
    
        
app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/spanish', SpanishPage),
    ('/japanese', JapanesePage),
    ('/vietnamese', VietnamesePage),
    ('/tagalog', TagalogPage),
    ('/english', EnglishPage),
    ('/spanishmood', SpanishMoodPage)
    # ('/englishmood', EnglishMoodPage),
    
], debug=True)