__author__ = 't'

class AuthenticationMixin(object):
    def get_authentication_representation(self, request):
        return {
            'email': request.user.email if request.user.is_authenticated() else None,
            'isAuthenticated': request.user.is_authenticated(),
            'id': unicode(request.user.pk) if request.user.is_authenticated() else None,
        }
