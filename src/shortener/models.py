from django.conf import settings
from django.db import models

# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com


# looks for settings attribute, if not present defaults to 15
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        # qs is queryset
        # qs_main is equivalent to built-in default for all
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            # reverses query set based on reversed order of ids
            # takes up to the last X items
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "new codes made: {i}".format(i=new_codes)

class KirrURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True) # when model last updated
    timestamp = models.DateTimeField(auto_now_add=True) # when model was created
    active = models.BooleanField(default=True)
    # empty_dateime = models.DateTimeField(auto_now=False, auto_now_add=False)
    # shortcode = models.CharField(max_length=15, null=True) empty in db is ok
    # shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    objects = KirrURLManager()
    some_random = KirrURLManager()


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

    def short_url(self):
        url_path = reverse("scode", kwargs={"shortcode": self.shortcode}, host="www", scheme="http")
        return url_path
        # return "http://www.tirr.com/{shortcode}".format(shortcode=self.shortcode)

'''
NOTE run these commands whenever touching models.py:
python manage.py makemigrations
python manage.py migrate
'''
