from django.urls import include, path
from . import views, views2
from .views import SubscriberSignUpView, PublisherSignUpView

urlpatterns = [
    path('subscribe', views.SubscriberSignUpView.as_view(),  name='subscribe'),
    path('publish', views.PublisherSignUpView.as_view(),  name='publish'),
    path('home', views2.home, name='home'),
    path('login', views2.login_user, name='login'),
    path('viewData', views2.viewData, name='viewData'),
    path('publisherEdit', views2.publisherEdit , name =  'publisherEdit')
]
