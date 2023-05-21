from django.urls import path
from moneyapp import views #ไว้เรียกใช้ views.py

urlpatterns = [
    path('',views.index), #ไว้ระบุพาทหน้าแรกให้เรียกใช้ views index
    path('account',views.account) #ไว้ระบุพาทหน้าแรกให้เรียกใช้ views account
]
