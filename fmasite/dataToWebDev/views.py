from django.shortcuts import render
import test

def index(request):
	return render(request, 'tabs/home.html')


def contact(request):
	return render(request, 'dataSets/outputFromPyFile.html', {'content': test.finalOutput()})