from django import forms

# from django.core.validators import URLValidator
from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget = forms.TextInput(
            attrs ={
                "placeholder": "Long URL",
                "class": "form-control"
            }
        )
    )

    # NOTE validates on the form
    # def clean(self):
    #     NOTE clean() is automatically called every time form valid method is called
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)
    #     url = cleaned_data.get('url')
    #     NOTE better to use cleaned_data.get('url') if field is required above
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     return url
    #     #print(url)

    # NOTE validates directly on an individual field (e.g. url)
    # NOTE need to use similiar clean_<field> syntax to validate on another field
    # def clean_url(self):
        # url = self.cleaned_data['url']
        # if "http" in url:
        #     return url
        # return "http://" + url
