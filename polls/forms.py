from django import forms


class NewItemForm(forms.Form):
    input_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Click Add or press Enter',
                'class': 'form-control',
                'aria-label': 'Type to add',
                'aria-describedby': 'inputGroup-sizing-default',
            }
        )
    )
