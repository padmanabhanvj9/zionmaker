import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)

def pad(request):
    
    ask = Ask(app, "/")
    logging.getLogger('flask_ask').setLevel(logging.DEBUG)


    @ask.launch
    def launch():
        speech_text = 'Welcome to Infocuit Solutions, you can say hello'
        return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


    @ask.intent('HelloWorldIntent')
    def hello_world():
        speech_text = 'Hello world'
        return statement(speech_text).simple_card('HelloWorld', speech_text)


    @ask.intent('AMAZON.HelpIntent')
    def help():
        speech_text = 'You can say hello to me!'
        return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


    @ask.session_ended
    def session_ended():
        return "{}", 200



