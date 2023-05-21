from django.contrib import admin
from moneyapp.models import Statement

class StatementAdmin(admin.ModelAdmin): #ไว้ปรับแต่งหลังบ้านของ admin
    list_display=["name","amount","category"]
    list_per_page = 5 #แสดงผลรายการในหน้า admin ตามจำนวนที่ระบุไว้
    list_editable=["amount","category"] #สามารถแก้ไขได้ในหน้าแรกของ admin
    list_filter=["category","amount"] # เป็นตัวกรองข้อมูลว่าเป็นรายรับหรือรายจ่าย
    search_fields=["name"] #เป็นช่องค้นหาข้อมูลในส่วนของ admin 

# Register your models here.
admin.site.register(Statement,StatementAdmin)