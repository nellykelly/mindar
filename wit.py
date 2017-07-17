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



class AI():
	def userinput(userinput):

		time = False
		alarm = False
		check = False
		what = False
		alarmclock = False
		chnage = True

		arr = userinput.split()
		print(arr)
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

		if alarm == True:
			"would you like to change, delete, or add an alarm?"

		if alarm == True && change == True:
			


	