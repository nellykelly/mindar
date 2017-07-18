# from wit import Wit
# import logging

# def send(request, response):
#     print('Sending to user...', response['text'])
# def my_action(request):
#     print('Received from user...', request['text'])





# class messages(ndb.Model):
#     content = ndb.StringProperty()


# class ChatHandler(webapp2.RequestHandler):
# 	def get(self):
# 		content = self.request.get('content')
# 		message = self.request.get('message')

# 		content_model = Content(content = content)
#         content_key = content_model.put()
#         print(message + " : user just said this")
# 		resp = client.message(message)


# 		template = jinja_environment.get_template('chat.html')
# 		self.response.out.write(template.render({
# 			'resp' :resp,
# 		}))


# 	def post(self):
# 		results_template = env.get_template('chatresponce.html')

# 		print('Yay, got Wit.ai response: ' + str(resp))



# actions = {
#     'send': send,
#     'my_action': my_action,
# }

# client = Wit(access_token=access_token, actions=actions)



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