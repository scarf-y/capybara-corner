from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'icikiwir',
        'price': '10000000',
        'description': 'this is capybara',
        'chill_level': '10'
    }

    return render(request, "main.html", context)