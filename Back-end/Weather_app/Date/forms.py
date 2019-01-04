from django import forms


class CityForm(forms.Form):
    city_name = forms.CharField(label='', max_length=12)


# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)