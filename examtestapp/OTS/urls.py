from django.urls import path
from OTS.views import *
urlpatterns = [
    path('', welcome),
    path('new-candidate/', candidateRegistrationForm, name='registrationForm'),
    path('store-candidate', candidateRegistration, name='store-candidate'),
    path('login', loginView, name='login'),
    path('home', candidateHome),
    path('test-paper', testPaper),
    path('calculate-result', calculateTestResult),
    path('test-history', testResultHistory),
    path('result', showTestResult),
    path('logout', logoutView),
]
