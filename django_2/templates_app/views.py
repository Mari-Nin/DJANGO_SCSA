from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponse
from .models import Post,Contact,Employee,Comment,Rates
from .forms import ContactForm,ContactModelForm,Employee,EmployeeModelForm,RatesModelForm

def home(request):
    return HttpResponse("Welcome to scsa_app")

def about(request):
    return render(request,'about.html')


def welcome_page(request):
    content={'name':'mari',
             'age':2}
    return render(request,'welcome_page.html',content)

def posts(request):
    posts=Post.objects.all()
    return render(request, 'posts.html',{'posts':posts})

def post_detail(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
        return HttpResponse(f"Title: {post.title}, content: {post.description}")
    except Post.DoesNotExist:
        raise Http404(f"Post with ID {post_id} does not exist")

def api_view(request):
    data = {'message': 'This is a simple API request',
            'status':'success',
            'number':'2026'}

    return JsonResponse(data)

@login_required
def protected_view(request):
    return HttpResponse('This is protected page')
def rates(request):
    if request.method=='POST':
        form = RatesModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templates_app:rates')
    else:
        form = RatesModelForm()
    rates = Rates.objects.all()

    context = {
            'form':form,
            'rates':rates}
    return render(request,'rates.html',context)
def edit_rate(request,rate_id):
    rate = Rates.objects.get(id=rate_id)
    rates=Rates.objects.all()
    if request.method =='POST':
        form = RatesModelForm(request.POST,instance=rate)
        if form.is_valid():
            form.save()
            return redirect('templates_app:rates')   
    else:
        form=RatesModelForm(instance=rate)   
    context={'form':form,
             'rate':rate,
             'rates':rates
             } 
    return render(request,'rates.html',context)
def delete_rate(request,rate_id):
    rate=Rates.objects.get(id=rate_id)
    rate.delete()
    return redirect('templates_app:rates')


def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            Contact.objects.create(name=name,email=email,message=message)
            return redirect('templates_app:contact')
        else:
            email_errors = form.errors.get('email',[])
            for error in email_errors:
                if 'ge'not  in error:
                    return HttpResponse('Only .ge is valid')
    else:
        form = ContactForm()
    contacts = Contact.objects.order_by('id')
    context = {
        'form':form,
        'contacts':contacts}
    return render(request,'contact.html',context)

def edit_contact(request,cont_id):
    contact = Contact.objects.get(id=cont_id)
    contacts=Contact.objects.all()
    if request.method =="POST":
        form  = ContactModelForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('templates_app:contact')
    else:
        form = ContactModelForm(instance=contact)
    context = {'form':form,
                'contact':contact,
                'contacts' :contacts}
    return render(request,'edit_employee.html',context)

def delete_contact(request,cont_id):
     contact=Contact.objects.get(id=cont_id)
     contact.delete()
     return redirect('templates_app:contact')


@login_required
def employee(request):
    if request.method =='POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templates_app:employee')
    
        else:
            employees = Employee.objects.all()
            context={
                'form':form,
                'employees':employees
            }
            return render(request, 'employee.html', context)
    else:
            form = EmployeeModelForm()
            employees = Employee.objects.all()
            context={
                'form':form,
                'employees':employees
            }
            return render(request,'employee.html', context)

def edit_employee(request,emp_id):
    employee = Employee.objects.get(id=emp_id)
    employees = Employee.objects.all()
    if request.method =="POST":
        form = EmployeeModelForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('templates_app:employee')
    else:
        form = EmployeeModelForm(instance=employee)
    context = {'form':form,
               'employee':employee,
                'employees' :employees}
    return render(request,'edit_employee.html',context)

@login_required
def delete_employee(request,emp_id):
    employee = Employee.objects.get(id = emp_id)
    employee.delete()
    messages.success(request,'Employee is deleted')
    return redirect('templates_app:employee')

  





