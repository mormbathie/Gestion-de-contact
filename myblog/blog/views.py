from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, redirect
from .models import Contact
from django.contrib.auth.decorators import login_required
def home(request):
    contacts = Contact.objects.all()
    return render(request,'pages/index.html',{'contacts':contacts})

def about(request):
    return render(request,'pages/about.html')

@login_required(login_url='/login/')
def contact(request):
    user = request.user
    print(user)
    contacts = Contact.objects.filter(author=user,archif=False)
    return render(request,'contacts/contact_list.html',{'contacts':contacts})

@login_required(login_url='/login/')
def contact_detail(request,id):
    contact = get_object_or_404(Contact,pk=id)
    return render(request, 'contacts/contact_detail.html',{'contact':contact})

@login_required(login_url='/login/')
def contact_create(request):
    if request.method == 'POST':
        author = request.user
        name = request.POST.get('nom')
        lastname = request.POST.get('prenom')
        phonenumber = request.POST.get('telephone')
        email = request.POST.get('email')
        contact = Contact.objects.create(
            name=name,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            author=author
        )
        contact.save()
        return redirect('/contact/')   
    return render(request,'contacts/contact_create.html')



def edit_contact(request,id):
    contact = get_object_or_404(Contact,id=id)
    if request.method == 'POST':
        name = request.POST['nom']
        lastname = request.POST['prenom']
        phonenumber = request.POST['telephone']
        email = request.POST['email']
        contact_to_update = Contact.objects.filter(pk=contact.id)
        contact_to_update.update(
            name=name,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
        )
        return redirect('/contact/')
   
    return render(request,'contacts/contact_edit.html',{'contact':contact})


def delte_contact(request,id):
    contact = get_object_or_404(Contact,id=id)
    if request.method == 'POST':
        contact_to_delete = Contact.objects.filter(pk=contact.id)
        contact_to_delete.update(
            archif=True
        )
        return redirect('/contact/')
    return render(request,'contacts/contact_delete.html',{'contact':contact})