from django.shortcuts import render

# Create your views here.
def mdb_bootstrap(request):
    return render(request,'mdb_bootstrap.html')
def carousel(request):
    return render(request,'carousel.html')
def bg_img(request):
    return render(request,'bg_img.html')