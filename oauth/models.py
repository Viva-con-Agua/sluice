from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
#class SluiceUsers(AbstractUser):
#    REQUIRED_FIELDS = ["email"]
import json
from django.core.serializers.json import DjangoJSONEncoder


class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """

    def to_python(self, value):
        if value == "":
            return None

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value



class SluiceUserManager(BaseUserManager):

    def _create_user(self, pool_id, token, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not pool_id:
            raise ValueError('NO USER_ID')
        #drops_id = self.normalize_email(email)
        user = self.model(pool_id= pool_id, token='',
                          is_staff=is_staff, is_active=True,
                          last_login=now,
                          date_joined=now, **extra_fields)
        #user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, pool_id, **extra_fields):
        return self._create_user(pool_id, '', False, False,
                                 **extra_fields)

    def create_superuser(self, pool_id, password, **extra_fields):
        return self._create_user(pool_id, password, True, True,
                                 **extra_fields)




class SluiceUser(AbstractBaseUser):
    pool_id = models.CharField(_('pool_id'), max_length=254, unique=True, primary_key=True, default='huhu')
   #first_name = models.CharField(_('first name'), max_length=30, blank=True)
   #last_name = models.CharField(_('last name'), max_length=30, blank=True)
    token = JSONField(max_length=254, null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_admin = models.BooleanField(default=False)

    objects = SluiceUserManager()

    USERNAME_FIELD = 'pool_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

#    def email_user(self, subject, message, from_email=None):
#        """
#        Sends an email to this User.
#        """
#        send_mail(subject, message, from_email, [self.email])


#class SluiceProfile(models.Model):
#    user = models.OneToField(User, on_delete=models.CASCADE)


