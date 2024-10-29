#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse("Fuck You")
   return render(request, 'home.html')

def premiership(request):
   # return HttpResponse("Fuck you too")
   return render(request, 'premiership.html')

def Belgian1(request):
   # return HttpResponse("Fuck you too")
   return render(request, 'belgian_pro_league.html')

def Championship(request):
   
   return render(request, 'championship.html') 

def League1(request):
 
   return render(request, 'league_one.html')

def League2(request):
 
   return render(request, 'english_league_two.html')


def GermanBundesliga(request):
 
   return render(request, 'german_bundesliga.html')

def GermanBundesliga2(request):
 
   return render(request, 'german_bundesliga_2.html')

def GreekSuperLeague(request):
 
   return render(request, 'greek_super_league.html')