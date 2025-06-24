#from django.shortcuts import render

# Create your views here.
"""
from django.shortcuts import render
def index(request):
 return render(request, 'holaapp/index.html')
"""
from django.shortcuts import render
from .forms import Valueform
from .clasificacion import clasifica


def index(request):
 if request.method == 'POST':
  form = Valueform(request.POST)
  if form.is_valid():
   parametro = form.cleaned_data['busqueda']
   prediccion = clasifica(parametro)
  return render(request, "index.html", {'form': form, 'prediccion': prediccion})
 else:
  form = Valueform(initial={'busqueda': '', })
  return render(request, "index.html", {'form': form})

