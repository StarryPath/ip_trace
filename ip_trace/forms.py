from django import forms


class trace_ip(forms.Form):
    ip = forms.TimeField()
