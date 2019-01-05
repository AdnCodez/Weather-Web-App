from django import forms


class CityForm(forms.Form):
    city_name = forms.CharField(label='', max_length=12, widget=forms.TextInput(attrs={'autocomplete':'off', 'placeholder':'City Name'}))
