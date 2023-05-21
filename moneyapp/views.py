from django.shortcuts import render
from django.http import HttpResponse # ไว้แสดงผลข้อความบนเว็บไซ
from moneyapp.models import Statement
from django.db.models import Sum

# Create your views here.
def index(request): #ไว้เอา index ไปแสดงผลหน้าเว็บไซ
      total_income = Statement.objects.filter(category="income").aggregate(Sum("amount")) #รายรับทั้งหมด
      total_expense = Statement.objects.filter(category="expense").aggregate(Sum("amount")) #รายจ่ายทั้งหมด
      return render(request,"index.html",{"income":total_income,"expense":total_expense})

def account(request): #ไว้เอา account ไปแสดงผลหน้าเว็บไซ
      data=Statement.objects.all()
      return render(request,"account.html",{"data":data})
