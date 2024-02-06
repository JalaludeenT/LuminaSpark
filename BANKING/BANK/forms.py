from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import CreateAccount, validate_phone_number
from datetime import datetime
from django import forms


class CreateAccountForm(ModelForm):
    class Meta:
        model = CreateAccount
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['materials_provide'].queryset = self.instance.materials_provide.all()

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        validate_phone_number(phone_number)
        return phone_number

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth and date_of_birth > datetime.today().date():
            raise ValidationError('Invalid date of birth.')
        return date_of_birth

    def clean_age(self):
        age = self.cleaned_data['age']
        if age and age < 18:
            raise ValidationError('Age must be 18 or older.')
        return age

    def clean_materials_provide(self):
        materials_provide = self.cleaned_data['materials_provide']
        if not materials_provide.exists():
            raise ValidationError('Please select the materials do you want.')
        return materials_provide

    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get('phone_number')
        mail_id = cleaned_data.get('mail_id')

        if CreateAccount.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Phone number already taken.')

        if CreateAccount.objects.filter(mail_id=mail_id).exists():
            raise ValidationError('E-mail id is already taken.')

        return cleaned_data

    def save(self, commit=True):
        account = super(CreateAccountForm, self).save(commit=False)
        if commit:
            account.save()
        return account

