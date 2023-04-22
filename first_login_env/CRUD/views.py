from django.shortcuts import redirect , render
from tarfile import ReadError
from .forms import EmpForm
from .models import crud


# Create your views here.


def emplist(request):
    cont = crud.objects.all()
    return render(request,"emplist.html", {'cont':cont})

def empform(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmpForm()
        else:
            emp= crud.objects.get(pk=id)
            form=EmpForm(instance=emp)
            #form.save()
        return ReadError(request,"empform.html", {'form': form})
    else:
        if id == 0:
         form = EmpForm(request.POST)
        else:
            emp= crud.objects.get(pk=id)
            form=EmpForm(request.POST,instance = emp)
        if form.is_valid():
            form.save()
        return redirect('/emplist')
def empdelete(request,id):
    emp= crud.objects.get(id=id)
    emp.delete()
    return redirect('/emplist')

