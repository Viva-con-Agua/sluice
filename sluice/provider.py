from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class DropsOAuth2Account(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('profileUrl')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar')

    def to_str(self):
        dflt = super(OAuth2Account, self).to_str()
        return self.account.extra_data.get('username', dflt)

class DropsOAuth2Provider(OAuth2Provider):
    id = 'drops'
    name = 'drops'
    def get_default_scope(self):
        return []

provider_classes = [DropsOAuth2Provider]
