from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'active_index': 'active'})