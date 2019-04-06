from api.views.users_views import SignInView, SignUpView
from django.urls import path

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
]
