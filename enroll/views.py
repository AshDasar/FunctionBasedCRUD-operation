from django.shortcuts import render, HttpResponseRedirect

from .models import SaveStudentData

from .forms import StudentRegistration
#sending form data to DB
def showdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            #em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=SaveStudentData(name=nm,password=pwd)
            reg.save()
            fm=StudentRegistration()
            
    else:
        fm=StudentRegistration()

        #retreiving data from DB
    stud=SaveStudentData.objects.all()
    return render( request,'enroll/addnshow.html',{'forms':fm, 'stu':stud})

#updating student data
def update_data(request, id):
    if request.method=='POST':
        pi=SaveStudentData.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=SaveStudentData.objects.get(pk=id)
            fm=StudentRegistration(instance=pi)     
        
        return render(request, 'enroll/update.html', {'forms':fm})



#deleting student data from DB
def delete_data(request,id):
    if request.method== 'POST':
        pi=SaveStudentData.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')