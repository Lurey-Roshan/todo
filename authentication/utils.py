
#from authentication.models import User
from django.contrib.auth.tokens import  PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self,user,timestamp):
		#return str(user.pk)+str(timestamp)+user.is_email_verified
		return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_email_verified))
		#return super()._make_hash_value(user, timestamp)

generate_token=TokenGenerator()
#to use it we must install six ie pip insrtall six
