from django.shortcuts import render
from django.http import HttpResponse
import magic

# Create your views here.

def index(reqest, a, b):
    return HttpResponse(f"{a} + {b} это {magic.magic(a, b)}")