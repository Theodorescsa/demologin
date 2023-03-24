from django.urls import path
from home import views

urlpatterns = [
    path('member/', views.MemberList.as_view()),

]