from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request, 'feed.html')
    
def ask(request):
    return render(request, 'ask.html')
