from django.shortcuts import render
from django.http import HttpResponse
from freecourse.static.searcher.search import give as meth


def index(request):
    if request.method == "POST":
        tosearch = request.POST['currencytoconvert']
        context = search(tosearch)
        print({'list': context})
        return render(request,'pages/home.html', {'list': context})
    return render(request, 'pages/home.html')




def search(tosearch):
    result = meth(tosearch)
    # print(f'calling method result \n {result}')
    return result
    

