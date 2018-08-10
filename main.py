import webapp2
from random import shuffle
import jinja2
import os
from google.appengine.ext import vendor
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
from google.cloud import translate
from requests_toolbelt.adapters import appengine
import six
appengine.monkeypatch()

# import cloudstorage as gcs
# from google.cloud import storage
# from gcloud import storage
# from gcloud import translate


# Imports the Google Cloud client library
#from google.cloud import translate

#libraries for APIs
from google.appengine.api import urlfetch
import json


"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
def test_api(): 
    text = "Hello"
    translate_client = translate.Client()
    print("********************************************************")
    print("inside test_api")
    results = translate_client.get_languages()
    print("got results")
    for language in results:
        print(u'{name}({language})'.format(**language))
    return results

# if isinstance(text, six.binary_type):
#     text = text.decode('utf-8')

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
# result = translate_client.translate(
#     text, target_language=')

# print(u'Text: {}'.format(result['input']))
# print(u'Translation: {}'.format(result['translatedText']))
# print(u'Detected source language: {}'.format(
#     result['detectedSourceLanguage']))
# Instantiates a client
#translate_client = translate.Client()

# The text to translate
moods = {
            "happyList" : ["Hi!", "How are you?","I am so happy to meet you"],
            "sadList" : ["I am sad.", "Are you sad?", "I am not sorry."],
            "angryList" : ["I do not like you.", "You make me very mad"],
            "neutralList" : ["Nah, I am good.", "Maybe next time", "Sure"],
            "quirkyList" : ["That is crazy!","You are crazy!", "Oh my goodness!"]
    }

text = 'How are you?'
target = 'jp'

def translate_text(text, language): 
    translate_client = translate.Client()
    # if isinstance(text, six.binary_type):
    #     text = text.decode('utf-8')
    
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=language)
    
    print(u'Text: {}'.format(result['input']))
    print "TRANSLATION IS!!!!!!"
    print unicode(result['translatedText']).encode('utf-8')
    # print result['translatedText'].encode('utf-8', 'replace').decode('utf-8')
    # print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    # return unicode(result['translatedText']).encode('utf-8')
    return result['translatedText']
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
        # results = test_api() 
        html_template = the_jinja_env.get_template('html/intro.html')
        # the_variable_dict = {
        #     "results" : results
        # }
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
        print("moodType")
        moodType = self.request.get('mood')
        print(moodType)
        if moodType == 'happy':
            happySpanishList =[]
            for phrase in moods["happyList"]:
                happySpanishList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['happyList'],
                "Other" : happySpanishList
            }
            print("The variabe dict")
            print(the_variable_dict)
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(the_variable_dict)) 
            # do this
            # 
        elif moodType == 'sad':
            sadSpanishList =[]
            for phrase in moods["sadList"]:
                sadSpanishList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['sadList'],
                "Other" : sadSpanishList
            }
            print("The variabe dict")
            print(the_variable_dict)
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(the_variable_dict))
            # do this
            
        elif moodType == 'angry':
            angrySpanishList =[]
            for phrase in moods["angryList"]:
                angrySpanishList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['angryList'],
                "Other" : angrySpanishList
            }
            print("The variabe dict")
            print(the_variable_dict)
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(the_variable_dict)) 
            # do this
            
        elif moodType == 'neutral': 
            neutralSpanishList =[]
            for phrase in moods["neutralList"]:
                neutralSpanishList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['neutralList'],
                "Other" : neutralSpanishList
            }
            print("The variabe dict")
            print(the_variable_dict)
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(the_variable_dict))
            # do this
            
        else:
            quirkySpanishList =[]
            for phrase in moods["quirkyList"]:
                quirkySpanishList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['quirkyList'],
                "Other" : quirkySpanishList
            }
            print("The variabe dict")
            print(the_variable_dict)
            neutral_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(neutral_template.render(the_variable_dict))
   
        
        # html = the_jinja_env.get_template('html/spanish.html')
class JapanesePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('html/japanese.html')
        self.response.write(about_template.render())
        
    def post(self): 
        moodType = self.request.get('mood')
        if moodType == 'happy':
            happyJapaneseList =[]
            for phrase in moods["happyList"]:
                happyJapaneseList.append(translate_text(phrase, 'ja'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['happyList'],
                "Other" : happyJapaneseList
            }
            print("The variabe dict")
            print(the_variable_dict)
            about_template = the_jinja_env.get_template('html/moods/happy.html')
            self.response.write(about_template.render(the_variable_dict)) 
            # do this
            # 
        elif moodType == 'sad':
            sadJapaneseList =[]
            for phrase in moods["happyList"]:
                happyJapaneseList.append(translate_text(phrase, 'es'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['sadList'],
                "Other" : sadJapaneseList
            }
            print("The variabe dict")
            print(the_variable_dict)
            sad_template = the_jinja_env.get_template('html/moods/sad.html')
            self.response.write(sad_template.render(the_variable_dict)) 
            # do this
            
        elif moodType == 'angry':
            angryJapaneseList =[]
            for phrase in moods["angryList"]:
                angryJapaneseList.append(translate_text(phrase, 'ja'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['angryList'],
                "Other" : angryJapaneseList
            }
            print("The variabe dict")
            print(the_variable_dict)
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(the_variable_dict))
            # do this
            
        elif moodType == 'neutral': 
            neutralJapaneseList =[]
            for phrase in moods["neutralList"]:
                neutralJapaneseList.append(translate_text(phrase, 'ja'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['neutralList'],
                "Other" : neutralJapaneseList
            }
            print("The variabe dict")
            print(the_variable_dict)
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(the_variable_dict)) 
            # do this
            
        else:
            quirkyJapaneseList =[]
            for phrase in moods["quirkyList"]:
                quirkyJapaneseList.append(translate_text(phrase, 'ja'))
            # List.append(elem)
            the_variable_dict={
                "English" : moods['quirkyList'],
                "Other" : quirkyJapaneseList
            }
            print("The variabe dict")
            print(the_variable_dict)
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(the_variable_dict)) 
        
        
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
            self.response.write(sad_template.render(moods['sadDict'])) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(moods['angryDict'])) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(moods['neutralDict'])) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(moods['quirkyDict']))
            
        
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
            self.response.write(sad_template.render(moods['sadDict'])) 
            # do this
            
        elif moodType == 'angry':
            angry_template = the_jinja_env.get_template('html/moods/angry.html')
            self.response.write(angry_template.render(moods['angryDict'])) 
            # do this
            
        elif moodType == 'neutral': 
            neutral_template = the_jinja_env.get_template('html/moods/neutral.html')
            self.response.write(neutral_template.render(moods['neutralDict'])) 
            # do this
            
        else:
            quirky_template = the_jinja_env.get_template('html/moods/quirky.html')
            self.response.write(quirky_template.render(moods['quirkyDict']))
            
    
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
#print(u'Translation: {}'.format(translation['translatedText'])
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