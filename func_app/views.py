from django.shortcuts import render
from django.http import HttpResponse
import magic

# Create your views here.

def index(reqest, req):
    return HttpResponse(f"Результат:\n{magic.magic(req)}")