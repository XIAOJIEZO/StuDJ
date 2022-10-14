from django.test import TestCase
from django.shortcuts import render

# Create your tests here.

def test777(request):
    return render(request, "base1.html")