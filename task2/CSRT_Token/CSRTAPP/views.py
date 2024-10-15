from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyData
from django.shortcuts import redirect, render

@csrf_exempt  
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def view_data(request):
    all_data = MyData.objects.all() # To fetch all saved data from the database

    return render(request, 'view_data.html', {'all_data': all_data}) # Render the data in a template

@csrf_exempt  
def save_data(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        data_entry = MyData(name=name, email=email, message=message)
        data_entry.save()

        
        return JsonResponse({'status': 'success', 'message': 'Data saved successfully!'})
    else:
        
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

