from django import forms
from .models import Products, Document
from .tasks import load_to_db_task


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class DocumentForm(forms.ModelForm):
    def save_to_db(self):
        load_to_db_task.delay()

    class Meta:
        model = Document
        fields = ('description', 'document')
