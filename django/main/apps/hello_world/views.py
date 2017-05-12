from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
def index(request):
    response = "Hello World!"
    return HttpResponse(response)

def index(request):
	return render(request, 'hello_world/index.html')
# def show(request):
# 	print request.method
# 	return render(request, 'hellow_world/showusers.html')
