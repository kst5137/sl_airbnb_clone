from django.shortcuts import render
from board.forms import BoardForm
from django.shortcuts import redirect

# Create your views here.
def register(request):
    if request.method == "GET":
        boardForm = BoardForm()
        return render(request, 'registertest.html', {'boardForm':boardForm})
    elif request.method == "POST":
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            return redirect('/boardRegister')