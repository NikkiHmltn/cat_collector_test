from django.shortcuts import render
# from django.http import HttpResponse

cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'cats/home.html')
    # return HttpResponse("hello")

def about(request):
    return render(request, 'cats/about.html')

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})