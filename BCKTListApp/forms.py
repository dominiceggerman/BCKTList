from django import forms

class TodoForm(forms.Form):
    
    text = forms.CharField(max_length=50,
        widget=forms.TextInput(
            # Attributes of input text field
            attrs={"class": "text-input", "placeholder": "Add an item to your BCKT List:"}
    ))
