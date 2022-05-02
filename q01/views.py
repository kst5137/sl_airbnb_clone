from django.shortcuts import render

# Create your views here.


def func1(abcde) :


    var1 = abcde.GET.get('var1',None)   # 변수 = 함수의 매개변수.GET.get('키에 해당하는 값',기본값)
    #매개변수에 저장된 데이터 중 get방식의 데이터만 가져오겠다.
    #뒤에 None은 안써줘도 됨 안썼을때 데이터를 안보내면 에러가 날 수 있기 때문에
    # var1에 기본값에 해당하는 값을 입력
    var2 = abcde.GET.get('var2', None)

    print(int(var1) * int(var2))

    return render(abcde, 'q01/func1.html')



def func2(abcde) :



    return render(abcde, 'q01/func2.html')





def func3(abcde) :

    var1 = abcde.POST.get("var1", None)
    var2 = abcde.POST.get("var2", None)

    print(var1)
    print(var2)
    print(int(var1) * int(var2))



    return render(abcde, 'q01/func3.html')