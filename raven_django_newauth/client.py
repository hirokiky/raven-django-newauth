from raven.contrib.django.client import DjangoClient


class NewauthClientMixin(object):
    def get_user_info(self, request):
        if request.auth_user.is_authenticated():
            user_info = {
                'is_authenticated': True,
                'id': request.auth_user.pk,
                'username': getattr(request.auth_user, 'username', None),
                'email': getattr(request.auth_user, 'email', None),
            }
        else:
            user_info = {
                'is_authenticated': False,
            }
        return user_info


class DjangoNewauthClient(NewauthClientMixin, DjangoClient):
    pass
