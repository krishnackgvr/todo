from django.shortcuts import render,redirect
from.models import Crud
from django.contrib import messages

# Create your views here.
def demo(request):
    crud1=Crud.objects.all()
    if request.method=="POST":
        slno=request.POST['slno']
        itemname=request.POST['itemname']
        description=request.POST['description']
        crud=Crud(slno=slno,itemname=itemname,description=description)
        crud.save()
        messages.info(request,"Data created successfully")
    return render(request,"base.html",{'res':crud1})
def delete(request,crudid):
    if request.method=='POST':
        crud=Crud.objects.get(id=crudid)
        crud.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request, id):
    contact1 = Crud.objects.all()
    contact = Crud.objects.get(id=id)

    if request.method == 'POST':
        slno = request.POST.get('slno', '')
        itemname = request.POST.get('itemname', '')
        description = request.POST.get('description', '')

        contact.slno = slno
        contact.itemname = itemname
        contact.description = description
        contact.save()

        return redirect('/')
    
    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})    
