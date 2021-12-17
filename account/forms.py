from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Subscriber, Users, PublisherData



class SubscriberForm(UserCreationForm):
    data = forms.ModelMultipleChoiceField(
        queryset= PublisherData.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = True
        
    )
    class Meta(UserCreationForm.Meta):
        model = Users
    
    def save(self):
        user = super().save(commit=False)
        user.is_subscriber = True
        user.save()
        subscriber = Subscriber.objects.create(user=user)
        subscriber.data.add(*self.cleaned_data.get('data'))
        
        return user
    
class PublisherForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_publisher = True
        if commit:
            user.save()
        return user
        
    
