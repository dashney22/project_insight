from django.shortcuts import render, redirect
from .models import Town

# Create your views here.

# View for veiwing all towns in the database {using DBSQLITE}
def home_view(request):
    if request.method == 'POST':
        new_town_name = request.POST.get('new_town_name')
        if new_town_name:
            Town.objects.create(name=new_town_name)  
            return redirect('home')  # Redirect to refresh town list
    
    towns = Town.objects.all()

    context = {
        'towns': towns,
    }
    return render(request, 'home.html', context)

