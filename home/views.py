from django.shortcuts import render

# Create your views here.
def vista_about(request):
    return render(request, 'about.html')

def vista_biografia(request):
    return render(request, 'bio.html')


def vista_inicio(request):
    return render(request, 'inicio.html')