from wit import Wit
import logging

def send(request, response):
    print('Sending to user...', response['text'])
def my_action(request):
    print('Received from user...', request['text'])





class messages(ndb.Model):
    content = ndb.StringProperty()


class chatHandler(webapp2.RequestHandler):
	def get(self):
		content = self.request.get('content')

		content_model = Student(content = content)
        content_key = content_model.put()
		print(userms + "user just said this")



		template = jinja_environment.get_template('chat.html')

		# self.response.out.write(template.render({
		# 	'' : ,
		# }))


	def post(self):




actions = {
    'send': send,
    'my_action': my_action,
}

client = Wit(access_token=access_token, actions=actions)