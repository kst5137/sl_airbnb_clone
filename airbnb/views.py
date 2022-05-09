from django.shortcuts import render

# Create your views here.
def index(abcde) :
    return render(abcde, 'index.html')
def hostpage_main(abcde) :
    return render(abcde, 'hostpage_main.html')
def login(abcde) :
    return render(abcde, 'login.html')
def register(abcde) :
    return render(abcde, 'host_register.html')
def room(abcde) :
    return render(abcde, 'room.html')
def register(abc):
    return render(abc, '/board/register.html')