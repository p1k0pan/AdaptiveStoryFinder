from django import forms


class HistoryForm(forms.Form):
    post = forms.CharField()