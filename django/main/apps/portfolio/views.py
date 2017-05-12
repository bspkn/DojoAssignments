from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
def index(request):
    response = "Welcome to My Portfolio!"
    return HttpResponse(response)

def index(request):
	return render(request, 'portfolio/index.html')
def show(request):
	print request.method
	return render(request, 'portfolio/testimonials.html')

# Create your views here.
