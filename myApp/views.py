from django.shortcuts import render

def index(request):
    return render(request, 'myApp/homePage.html')
def contact(request):
    return render(request, 'myApp/basic.html', {'values': ['Если у Вас осталист вопросы, то задавайтесь их по телефону', '(068) 068-68-68', 'e-mail: aaa@bbb.com.aa']})
