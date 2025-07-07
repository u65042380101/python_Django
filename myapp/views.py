from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages 

# Create your views here.
def index(request):
    all_person = Person.objects.order_by('id')  # เรียงตามลำดับที่สร้าง (ไม่เปลี่ยนเมื่อแก้ไข)
    return render(request, 'index.html', {'all_person': all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]

        # บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
        # เปลี่ยนเส้นทางไปยังหน้าแรกหลังจากบันทึกข้อมูล
        return redirect("/")
    else:
        return render(request,"form.html")  
    
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id) 
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "อัพเดตข้อมูลเรียบร้อยแล้ว")

        return redirect("/")
    else:
        # ดึกข้อมูลของบุคคลที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)    
        return render(request,"edit.html", {"person": person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")

    return redirect("/")