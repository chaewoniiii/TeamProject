from django.shortcuts import render

# # Create your views here.
def rt_create(request):
    return render(request, 'rt_create.html')