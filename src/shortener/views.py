from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.
def test_view(request):
    return HttpResponse("test")

# function-based view
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    # NOTE: deprecated in favor of get_object_or_404
    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists():
    #     obj = qs.first()
    #     obj_url = obj.url

    obj = get_object_or_404(KirrURL, shortcode=shortcode)

    # return HttpResponse("hello {sc}".format(sc=obj_url))
    return HttpResponseRedirect(obj.url)


# class-based view
class KirrCBView(View):
    # class-based views must explicitly handle http methods whereas function-based view handles everything automatically and method can be accessed with request.method
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        # return HttpResponse("hello again {sc}".format(sc=shortcode))
        return HttpResponseRedirect(obj.url)
