from django.shortcuts import render
from django.http import HttpResponse, response

from .forms import ItemForm
# Create your views here.
def home(request):
    request.session.set_test_cookie() # this will set a randoom cookie to server
    '''this method will internally set a cookie 
    and the browse should accept that cookie .if it accept
    that cookie when the browser from the very same browser we access the 
    second page of the application we are checking if hte browser is sending that cooke
    back'''
    return HttpResponse("<h2> Home page<h2>")


def page2(request):
    if request.session.test_cookie_worked():
        print('cookie are enabled')
        request.session.delete_test_cookie()
    return HttpResponse("<h1>page2<h1>")

def countview(request):
    if 'count' in request.COOKIES:
        
        count=int(request.COOKIES['count'])+1
    else:
        count=1
    response=render(request, 'cookie.html',{'count':count})
    print(response)
    response.set_cookie('count',count)
    return response

def index(request):
    return render(request, 'index.html')
def addItem(request):
    form=ItemForm()
    response=render(request, 'addItem.html',{'form':form})
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 120) # third arg is timeout in sec
    return response
def displayCart(request):
    return render(request, 'displayItems.html')








    # session  api, like above pagecount
def pageCount(request):
    count = request.session.get('count',0) 
    '''request.session.get('count',0) this will give us access to the current session
    .get is the method using which we can retrieve the value within the session count
    we have n't set this at this moment so if it is blank we can return a default value of it
    it is not there we are telling the get method to return a 0(zero) it this key doesn't
    exist in the session yet,assigned this to a variable called count.
    '''
    count= count+1
    request.session['count']=count # this is where we are setting the into session dictionary
    return render(request,'cookie.html',{'count':count})



def index(request):
    return render(request, 'index.html')
def addItemSession(request):
    form=ItemForm()
    
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            quantity=form.cleaned_data['quantity']
            request.session[name]=quantity
    return render(request,'addItemSession.html',{'form':form})
def displayCartSession(request):
    return render(request, 'displayItemSession.html')
