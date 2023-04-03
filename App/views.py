from django.shortcuts import render
import math 
# Create your views here.

def home(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        activity = request.POST.get('activity')
        age = request.POST.get('age')

        age = int(age)
        weight = int(weight)
        height = int(height)

        BMR = 0
        AMR = 0
        if gender == 'female':
            BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        else:
            BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

        if activity == 'sedentary':
            AMR = BMR * 1.2
        elif activity == 'Lightly active':
            AMR = BMR * 1.375
        elif activity == 'Moderately active':
            AMR = BMR * 1.55
        elif activity == 'Active':
            AMR = BMR * 1.725
        elif activity == 'Very active':
            AMR = BMR * 1.9
        AMR = math.ceil(AMR)
        return render(request, 'home.html', {'Calorie' : AMR})
    return render(request, 'home.html')
