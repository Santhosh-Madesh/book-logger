from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    review = forms.CharField(widget=forms.Textarea())
    rating = forms.IntegerField(max_value=5,min_value=1)