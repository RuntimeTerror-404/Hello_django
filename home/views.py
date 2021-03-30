from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def services(request):
    # return HttpResponse("all the services are here")
    return render(request, "services.html")

def contacts(request):
    # return HttpResponse("you can contact now")
    return render(request, "contacts.html")

def hello(request):
    return HttpResponse("hey, Good Morning")

def about(request):
    # return HttpResponse("we are ice cream seller in Noida") 
    return render(request, "about.html")

def stall(request):
    # return HttpResponse("this stall provides lot of varieties of ice creams")
    return render(request, "services.html")

def online(request):
    # return HttpResponse("we also have online store on amazon and flipkart")
    return render(request, "services.html")

# Create your views here.
