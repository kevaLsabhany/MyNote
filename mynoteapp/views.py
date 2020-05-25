from django.shortcuts import render,redirect
from .models import Note
import datetime

# Create your views here.
def index(request):
    notes = Note.objects.order_by("-time")
    context={'notes':notes}
    return render(request, 'mynoteapp/index.html', context)

def addNote(request):
    title = request.POST.get("title","")
    description = request.POST.get("description","")
    if title !="" and description !="" :
        Note.objects.create(title=title,description=description,date=datetime.date.today(),time=datetime.datetime.today()).save()
    return redirect("home")

def deleteNote(request,id):
    obj = Note.objects.get(id=id)
    obj.delete()
    return redirect("home")


