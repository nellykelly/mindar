#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import random
import logging
import webapp2
import jinja2
import os
import urllib
import urllib2
import json
from wit import Wit
import logging

import webapp2
from datetime import datetime
'''datetime library --->   https://docs.python.org/3/library/datetime.html#datetime.date'''
from datetime import timedelta
import time 
'''time format ---> https://docs.python.org/2/library/time.html#time.strftime'''
'''time library  --->    https://docs.python.org/2/library/time.html'''


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



#THIS IS WHERE WIT IS
def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])


class messages(ndb.Model):
    content = ndb.StringProperty()




actions = {
    'send': send,
    'my_action': my_action,
}

client = Wit(access_token=OKSUUQPRQUJD6CLD2GINQGA47UR7TBX4, actions=actions)

#END WIT

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('')
        template = jinja_environment.get_template('index.html')
class RemHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('')

class ChatHandler(webapp2.RequestHandler):
	def get(self):
		content = self.request.get('content')
		message = self.request.get('message')

		content_model = Content(content = content)
        content_key = content_model.put()
		print(message + " : user just said this")
		resp = client.message(message)


		template = jinja_environment.get_template('chat.html')
		self.response.out.write(template.render({
			'resp' :resp,
		}))


	def post(self):
		results_template = env.get_template('chatresponce.html')

		print('Yay, got Wit.ai response: ' + str(resp))




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/chat', Chathandler)
], debug=True)




x = datetime.now()
''' date format = (year, month, day, hour, minutes, seconds, milliseconds)'''
Event_List = {}

'''x = datetime.now().replace(microsecond=0)'''
today = (time.strftime("%m-%d-%Y"))
print today
def remind ():
	Event = raw_input("What do you have to do?")
	month = int(raw_input("What month?"))
	day = int(raw_input("What day?"))
	year = int(raw_input("What year?"))
	DateOfEvent = str(month+"-"+day+"-"+year)

'''gives the current day where 0 is Monday and 6 is Sunday'''
'''
Current_Time = current time at the moment
def remind("Event"):
	ask the question "What do you want to do?"
	save answer as a variable --> "Event" --> posssibly a dictionary
	ask "What time?"
	save the answer as a key of Event
	ask "Where?"
	save the answer as a key of Event
	"Event" = {time, place}'''



'''BRIEF DESCRIPTION INCOMING
When website is opened it should check the day and time
	today = time.localtime().tm_wday
	If its already open then maybe it should refresh every min or so
When USER clicks REMIMD button it should take them to a form
	The form ask for the EVENT and the DATE/TIME for the event
	The EVENT is then saved as a dictionary with the DATE/TIME as keys
	Maybe these are saved locally?
If the website is checking and it detects a key with the current date
	it has an alert or something pop up displaying the EVENT name and time
	'''
