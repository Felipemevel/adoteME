from django.shortcuts import render

def renderizar_index(request):
    return render(request, 'animais/index.html')

def renderizar_adotar(request):
    return render(request, 'animais/adotar.html')

def renderizar_abrigar(request):
    return render(request, 'animais/abrigar.html')    
