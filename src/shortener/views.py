from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.
# def test_view(request):
#     return HttpResponse("test")


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Kirr.co",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("url"))
        context = {
            "title": "Kirr.co",
            "form": form
        }

        return render(request, "shortener/home.html", context)

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
