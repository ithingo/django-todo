from django import forms


class NewItemForm(forms.Form):
    input_text = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Click Add or press Enter',
                'class': 'form-control',
                'aria-label': 'Type to add',
                'aria-describedby': 'inputGroup-sizing-default',
                'name': 'input_text',
            },
        ),
    )


class TabSwitchForm(forms.Form):
    TABS_SWITCHERS = (
        ('all', 'All'),
        ('checked', 'Checked'),
        ('unchecked', 'Unchecked'),
    )
    tabs = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'onclick': 'this.form.submit();',
                'class': 'tabs',
                'role': 'tab',
            }
        ),
        choices=TABS_SWITCHERS,
    )
