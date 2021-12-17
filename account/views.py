from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from .forms import SubscriberForm, PublisherForm

from .models import Users

# Create your views here.

class SubscriberSignUpView(CreateView):
    model = Users
    form_class = SubscriberForm
    template_name = 'subscriberReg.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'subscriber'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('account/subscribe')


class PublisherSignUpView(CreateView):
    model = Users
    form_class = PublisherForm
    template_name = 'publisherReg.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'subscriber'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('account/publish')
    

      
def home(request):        
    context = {}
    render(request, 'home.html', context)
     
    



    

