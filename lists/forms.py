from django import forms

from .models import Item


EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.ModelForm):
    # item_text = forms.CharField(
    #     widget=forms.fields.TextInput(attrs={
    #         'placeholder': 'Enter a to-do item',
    #         'class': 'form-control input-lg',
    #     }),
    # )
    class Meta:
        model = Item
        fields = ('text',)
        widgets= {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }