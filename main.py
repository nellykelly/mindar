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

import webapp2
from datetime import datetime
'''datetime library --->   https://docs.python.org/3/library/datetime.html#datetime.date'''
from datetime import timedelta
import time 
from google.appengine.ext import ndb
'''time format ---> https://docs.python.org/2/library/time.html#time.strftime'''
'''time library  --->    https://docs.python.org/2/library/time.html'''


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Message(ndb.Model):
	message = ndb.StringProperty()



class AI():
	def userinput(self, userinput):

		time = False
		alarm = False
		check = False
		what = False
		alarmclock = False
		chnage = True
		reminder = True


		arr = userinput.split()
		logging.info(arr)
		for i in arr:
			if i == "alarm":
				alarm = True
			if i == "check":
				check = True
			if i == "what":
				what = True
			if i == "alarmclock":
				alarmclock = True
			if i == "change":
				change = True
			if i == "reminder":
				reminder = True

		

		if alarm == True and change == True:
			return "Sorry, you cant change your alarm yet. You can delete it and create another though"


		if alarm == True and delete == True:
			logging.info("alarm")
			return "ok deleting the alarm now"


		if alarm == True or alarmclock == True:
			logging.info("alarm")
			return "would you like to change, delete, or add an alarm?"

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('indexform.html')
        self.response.out.write(template.render())

class RemOutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('indexform_out.html')
        self.response.out.write(template.render({
            'event' :self.request.get("eventName"),
            'date' :self.request.get("dayOfEvent"),
            'rem' :self.request.get("remindDate"),
		}))




class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())
    def post(self):
        event = self.request.get("eventName")
        date = self.request.get("dayOfEvent")
        remind = self.request.get("remindDate")
        date = datetime.strptime(date,("%m-%d-%Y")).date()
        event_model = EventModel(event = event, eventDate = date, remindWhen = remind).put()

class EventModel(ndb.Model):
	event = ndb.StringProperty()
	eventDate = ndb.DateProperty()
	remindWhen = ndb.StringProperty()

class RemHandler(webapp2.RequestHandler):
	def get(self):
		EventList = {}
		self.response.write('')
		template = jinja_environment.get_template("indexform.html")
		self.response.out.write(template.render())
		EventList["dayOfEvent"] = "eventName"
		EventList = EventModel.query().fetch()
	def post(self):
		template = jinja_environment.get_template("indexform_out.html")
		self.response.out.write(template.render())
		event = self.request.get("eventName")
		date = self.request.get("dayOfEvent")
		remind = self.request.get("remindDate")
		date = datetime.strptime(date,("%m-%d-%Y")).date()
		event_model = EventModel(event = event, eventDate = date, remindWhen = remind).put()
		



class ChatHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('chat.html')

#		content = self.request.get('content')
		message = self.request.get('message')

		message_model = Message(message = message)
		message_key = message_model.put()

		ai = AI()
		responce = ai.userinput(message)

		template = jinja_environment.get_template('chat.html')
		self.response.out.write(template.render({
            'resp' :responce,
		}))
        
	def post(self):
		results_template = env.get_template('chatresponce.html')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/chat', ChatHandler),
    ('/index', IndexHandler),
    ('/remout', RemOutHandler),
    ('/reminder', RemHandler)
], debug=True)




x = datetime.now()
''' date format = (year, month, day, hour, minutes, seconds, milliseconds)'''
Event_List = {}

'''x = datetime.now().replace(microsecond=0)'''
today = (time.strftime("%m-%d-%Y"))
print today
def remind ():
	Event = str(raw_input("What do you have to do?"))
	month = str(raw_input("What month?"))
	day = str(raw_input("What day?"))
	year = str(raw_input("What year?"))
	Date = datetime.date(yea, month, day)
	DateOfEvent = str(month+"-"+day+"-"+year)
	if today in EventList:
		print EventList[today]













# '''gives the current day where 0 is Monday and 6 is Sunday'''
# '''
# Current_Time = current time at the moment
# def remind("Event"):
# 	ask the question "What do you want to do?"
# 	save answer as a variable --> "Event" --> posssibly a dictionary
# 	ask "What time?"
# 	save the answer as a key of Event
# 	ask "Where?"
# 	save the answer as a key of Event
# 	"Event" = {time, place}'''



# '''BRIEF DESCRIPTION INCOMING
# When website is opened it should check the day and time
# 	today = time.localtime().tm_wday
# 	If its already open then maybe it should refresh every min or so
# When USER clicks REMIMD button it should take them to a form
# 	The form ask for the EVENT and the DATE/TIME for the event
# 	The EVENT is then saved as a dictionary with the DATE/TIME as keys
# 	Maybe these are saved locally?
# If the website is checking and it detects a key with the current date
# 	it has an alert or something pop up displaying the EVENT name and time
# 	'''