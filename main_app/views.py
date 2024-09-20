from django.shortcuts import render

# Create your views here.

# Add the Cat class & list and view function below the imports
class Rock:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, description, size):
    self.name = name
    self.color = color
    self.description = description
    self.size = size

rocks = [
    Rock('rocky','brown','was cast in a movie','big'),
    Rock('stone','grey','always stoned','medium'),
    Rock('pebble','white','annoying','small'),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rocks_index(request):
    return render(request,'rocks/index.html', {'rocks':rocks})