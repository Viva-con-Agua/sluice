from social_core.backends.oauth import BaseOAuth2

class Pool2OAuth2(BaseOAuth2):
    """Pool2 OAuth authentication backend"""
    name = 'drops'
    AUTHORIZATION_URL = 'sluice_auth'
    ACCESS_TOKEN_URL = 'sluice_token'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]

    def get_user_details(self, response):
        """Return user details from GitHub account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://api.github.com/user?' + urlencode({
            'access_token': access_token
        })
        return self.get_json(url)

