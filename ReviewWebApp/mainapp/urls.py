from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="signup"),
    path('Reviews',views.Reviews,name="Reviews"),
    path('logout',views.logout,name='logout'),
    path('fetch',views.fetch,name='fetch'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]