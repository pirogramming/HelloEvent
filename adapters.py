from allauth.account.utils import user_username, user_email, user_field
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import valid_email_or_none
from django.contrib.auth.models import UserManager as DefaultUserManager

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        social_app_name = sociallogin.account.provider.upper()
        if social_app_name =="GOOGLE":
            username = data.get('last_name')+data.get('first_name')
        else:
            username = data.get('username')

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user
        user_username(user, username or '')
        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        return user
