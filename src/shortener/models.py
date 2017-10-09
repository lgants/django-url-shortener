from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True) # when model last updated
    timestamp = models.DateTimeField(auto_now_add=True) # when model was created
    # empty_dateime = models.DateTimeField(auto_now=False, auto_now_add=False)
    # shortcode = models.CharField(max_length=15, null=True) empty in db is ok
    # shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    # overwrites default save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            # calls the default method by getting the super class of KirrURL
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

'''
NOTE run these commands whenever touching models.py:
python manage.py makemigrations
python manage.py migrate
'''