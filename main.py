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
import webapp2
from datetime import timedelta
from datetime import datetime
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('')

class RemHandler(webapp2.RequestHandler):
	def get(self):



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)



x = datetime.now()
Event = raw_input("What do you have to do?")
'''x = datetime.now().replace(microsecond=0)'''

'''
Current_Time = current time at the moment
def remind("Event"):
	ask the question "What do you want to do?"
	save answer as a variable --> "Event" --> posssibly a dictionary
	ask "What time?"
	save the answer as a key of Event
	ask "Where?"
	save the answer as a key of Event
	"Event" = {time, place}


