from django.http import HttpResponse
from django.shortcuts import render
import operator

def egg(request):
    return HttpResponse('<h1> hello  eggs</h1>')

def home_page(request):
    return render(request,'homepage.html',{'msg':'hi from view page'})

def count(request):
    text = request.GET['fulltext']
    word_list = text.split()
    word_number =len(word_list)
    dictionary={}
    for w in word_list:
        if(w in dictionary):
            dictionary[w]+=1
        else:
            dictionary[w]=1
    s = sorted(dictionary.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'text':text ,'number':word_number,'word_list':s})
def about(request):
    return render(request,'about.html')