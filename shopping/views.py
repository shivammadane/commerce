from django.shortcuts import render
from .models import *
from django.http import *
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

from http import *
# Create your views here.
def allcat():
    allcat = Category.objects.all()
    return allcat

def mycartdata(User=None):
    cartlist = []
    if User.is_authenticated:
        cart=AddToCart.objects.filter(usr=User)[::-1]
        cartlist=cart[:2]
    return cartlist

def comment(request,pid):
    us=request.user
    p=Product.objects.get(id=pid)
    m=request.POST['Comment']
    d=date.today()
    new.objects.create(u=us,p=p,m=m,d=d)
    return redirect('prod',pid)

'''
def sendemail(user,order):
   checkout_detail=order_product.objects.filter(id = order)
   Totalprice=0
   product_detail=order_product_detail.objects.filter(order_detail = checkout_detail)
   for i in product_detail:
       Totalprice+=i.total_amount
   name=user.first_name
   to_email=user.email
   from_mail=settings.EMAIL_HOST_USER
   sub='Confirmation Mail'
   msg=EmailMultiAlternatives(sub,' ',from_mail,[to_email])
   d={'product_detail':product_detail,'name':name,'totalprice':Totalprice}
   html=get_template('mail.html').render(d)
   msg.attach_alternative(html,'text/html')
   msg.send()
'''
def regmail(usr):
    name = usr.first_name
    us= usr.username
    to_email = usr.email
    from_mail = settings.EMAIL_HOST_USER
    sub = 'Registered Successfully'
    msg = EmailMultiAlternatives(sub, ' ', from_mail, [to_email])
    d = {'name': name,'us':us}
    html = get_template('regmail.html').render(d)
    msg.attach_alternative(html, 'text/html')
    msg.send()

def home(request):
    cat = Category.objects.all()
    data=Product.objects.all()
    fg=data[1:6:2]
    data1=data[9:12]
    new=data[0:1]
    cat=cat[3:4]
    d={"allcat":allcat,'mycart':mycartdata(request.user),'fg':fg,'data':data1,"cat":cat,"new":new}
    return render(request,'index.html',d)

def logi(request):
    error = False
    if request.method=='POST':
        use=request.POST
        u=use['uname']
        p=use['pwd']
        user=authenticate(username=u,password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {"allcat": allcat(),"error":error,'mycart':mycartdata(request.user)}
    return render(request, 'login.html',d)
def logou(request):
    logout(request)
    return redirect('home')
def signu(request):
    error = False
    if request.method=="POST":
        sigdata=request.POST
        f=sigdata['f']
        l=sigdata['l']
        pp=request.FILES['p']
        m=sigdata['mob']
        add=sigdata['ad']
        em=sigdata['ename']
        uname=sigdata['u']
        passw=sigdata['pwd']
        user = User.objects.filter(username=uname)
        if not user:
            userdata=User.objects.create_user(first_name=f,last_name=l,username=uname,password=passw,email=em)
            userdetail.objects.create(usr=userdata,mob=m,address=add,img=pp)
            regmail(userdata)
            return redirect('login')
        else:
            error = True
    d = {"allcat": allcat,'mycart':mycartdata(request.user),'error':error}
    return render(request,'signin.html',d)
'''
def forget(request):
    if request.method=='POST':
        E=request.POST
        e=E['email']
        user = authenticate(email=e)
        if user:
            login(request, user)
            if request.user.is_staff:
                return redirect('home')

    d = {"allcat": allcat,'mycart':mycartdata(request.user)}
    return render(request,'forget-password.html',d)
def forget1(request):
    d = {"allcat": allcat,'mycart':mycartdata(request.user)}
    return render(request,'forget-password2.html',d)'''
def aboutus(request):
    d = {"allcat": allcat,'mycart':mycartdata(request.user)}
    return render(request,'about.html',d)
def contact(request):
    d = {"allcat": allcat,'mycart':mycartdata(request.user)}
    return render(request,'contact.html',d)
def mega(request,sid):
    subcatdata=Subcategory.objects.get(id=sid)
    pro=Product.objects.filter(Subcat=subcatdata)
    paginator=Paginator(pro,3)
    page=request.GET.get('page',1)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
    othersubcat=Subcategory.objects.filter(cat=subcatdata.cat)[:4]
    d = {"allcat": allcat,"allpro":products,"othersub":othersubcat,'mycart':mycartdata(request.user)}
    return render(request,'shop.html',d)
def prodetail(request,pid):
    pro=Product.objects.get(id=pid)
    prodata=pro.Subcat
    p=Product.objects.filter(Subcat=prodata)
    ms=new.objects.filter(p=pro)
    sizelist=[]
    if pro.size:
        sizelist=pro.size.split(',')
    d = {"allcat": allcat,'detail':pro,'p':p,'size':sizelist,'mycart':mycartdata(request.user),'ms':ms}
    return render(request,'product-single.html',d)

def addtocarttable(request,pid):
    prodata=Product.objects.get(id=pid)
    user=request.user
    cartdata=AddToCart.objects.filter(usr=user,pro=prodata).first()
    if request.method=="POST":
      q=request.POST['quantity']
      size=[]
      total=int(prodata.price)*int(q)
      if cartdata:
          cartdata.quantity += int(q)
          cartdata.totalprice += total
          cartdata.save()
      else:
            AddToCart.objects.create(usr=user,pro=prodata,totalprice=total,quantity=q,size=size)
    return redirect('mycart')

def cart(request):
    my=AddToCart.objects.filter(usr=request.user)
    total = 0
    for i in my:
        total+=i.totalprice
    d = {"allcat": allcat,'my':my,'mycart':mycartdata(request.user),'total':total}
    return render(request,'cart.html',d)

def remove_from_cart(request,sid):
    data=AddToCart.objects.get(id=sid)
    data.delete()
    return redirect('mycart')


headers = { "X-Api-Key": "d36226f15fb5b59fbb817737f9068b10",
            "X-Auth-Token": "7db341777fe6acb02029ed77f9aa0178"}
import requests
import json
def payment(user,amount,order_id):
    payload={
        'purpose':'Product Payment',
        'buyer_name':user.username,
        'email':user.email,
        'phone':+918421707636,
        'amount':amount,
        'send_email':True,
        'send_sms':True,
        'redirect_url':' http://127.0.0.1:8000/paymentcheck/'+str(order_id)+'/'
    }
    url='https://www.instamojo.com/api/1.1/payment-requests/'
    response=requests.post(url,data=payload,headers=headers)

    print(response)
    res=response.text
    y=json.loads(res)
    print("dictionary.........",y)
    payment_id=y['payment_request']['id']
    long_url=y['payment_request']['longurl']
    return payment_id,long_url


def payment_check(request,order_id):
    order_data=order_product.objects.get(id=order_id)
    payment_id=order_data.payment_id
    url = 'https://www.instamojo.com/api/1.1/payment-requests/'+str(payment_id)+'/'
    response=requests.get(url,headers=headers)
    res=response.text
    y=json.loads(res)
    print("After----",y)
    status=y['payment_request']['status']
    d = {'data': order_data,'status': status,"allcat":allcat,'mycart':mycartdata(request.user)}
    if status=='Completed':
        order_data.payment_status='Done'
        order_data.save()
        pro_order_data=order_product_detail.objects.filter(order_detail= order_data)
        for i in pro_order_data:
            i.status='Order Confirmed'
            i.save()
            prodata=Product.objects.get(id=i.pro.id)
            q=i.quantity
            prodata.stock -= q
            prodata.save()
            cart=AddToCart.objects.filter(usr=request.user,pro=i.pro)
            cart.delete()
        return render(request,'confirmation.html',d)
    else:
        return render(request,'confirmation.html',d)



import random
def check(request,cid):
    form = orderform()
    if cid != 'All':
        cartdata=AddToCart.objects.filter(id=cid)
    elif cid == 'All':
        cartdata = AddToCart.objects.filter(usr=request.user)
    totalpayamount=0
    for i in cartdata:
        totalpayamount += i.totalprice
    if request.method == 'POST':
        form=orderform(request.POST)
        if form.is_valid():
            data=form.save()
            data.usr=request.user
            data.amount=totalpayamount
            ran=random.randint(100000,999999)
            data.order_id=ran
            data.date=date.today()
            data.save()
            payid,longurl=payment(request.user,totalpayamount,data.id)
            data.payment_id=payid
            data.save()
            expdate=date.today()+timedelta(5)
            for i in cartdata:
                order_product_detail.objects.create(order_detail=data,pro=i.pro,quantity=i.quantity,total_amount=i.totalprice,estimated_date=expdate)
            return redirect(longurl)
    d = {"allcat": allcat,'mycart': mycartdata(request.user),'form':form,'cartdata':cartdata,'grandtotal':totalpayamount}
    return render(request,'shipping.html',d)

def userdashboard(request,type):
    c1 = ''
    c2 = ''
    c3 = ''
    c4 = ''
    data =[]
    ud = []
    new = []
    if type == 'Allorder':
        c1 = 'active'
        order_data=order_product.objects.filter(usr=request.user)
        for f in order_data:
            alldata=order_product_detail.objects.filter(order_detail=f)
            for i in alldata:
                if i.status == 'Delivered':
                    data.append(i)
    elif type == 'Pending':
        c2 = 'active'
        order_data = order_product.objects.filter(usr=request.user)
        for f in order_data:
            alldata = order_product_detail.objects.filter(order_detail=f)
            for i in alldata:
                if i.status != 'Delivered':
                    data.append(i)
    elif type == 'Address':
        c3 = 'active'
        new=order_product.objects.filter(usr=request.user)

    elif type == 'Userdetail':
        c4 = 'active'
        ud = userdetail.objects.filter(usr=request.user).first()

    else:
        raise Http404()
    d={'type':type,'class1':c1,'class2':c2,'class3':c3,'class4':c4,'data':data,'ud':ud,'new':new,"allcat":allcat,'mycart':mycartdata(request.user)}
    return render(request,'dashboard.html',d)

def track(request,tid):
    tra=order_product_detail.objects.filter(id=tid)
    d={'track':tra,"allcat":allcat,'mycart':mycartdata(request.user)}
    return render(request,'track.html',d)


def add_edit(request):
    form = addproduct()
    if request.method == "POST":
        form = addproduct(request.POST,request.FILES)
        if form.is_valid():
            data = form.save()
            return redirect('meg',data.Subcat.id)
    d = {'form':form,"name":"Add New","name1":"Add","allcat":allcat,'mycart':mycartdata(request.user),"edit":'Add New'}
    return render(request,'add_edit_product.html',d)

def add_subcat(request):
    form=subcat()
    if request.method == 'POST':
        form=subcat(request.POST)
        if form.is_valid():
            data=form.save()
            return redirect('home')
    d={'form':form,"allcat":allcat,'mycart':mycartdata(request.user)}
    return render(request,'addsubcat.html',d)

def add_cat(request):
    form=addcat()
    if request.method == "POST":
        form=addcat(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    d={'form':form,"allcat":allcat,'mycart':mycartdata(request.user)}
    return render(request,'addcat.html',d)

def edit_pro(request,pid):
    prodata=Product.objects.get(id=pid)
    form = addproduct(instance=prodata)
    if request.method == "POST":
        form = addproduct(request.POST or None,request.FILES or None,instance=prodata)
        if form.is_valid():
            data = form.save()
            return redirect('prod',pid)
    d = {'form': form, "allcat": allcat, 'mycart': mycartdata(request.user),"prodata":prodata,"edit":"Edit:"+prodata.name,"name1":"edit"}
    return render(request, 'add_edit_product.html', d)

def delete_details(request,did,type):
    if type == 'Category':
        data=Category.objects.get(id=did)
        data.delete()
    elif type == 'SubCategory':
        data=Subcategory.objects.get(id=did)
        data.delete()
    elif type == 'Product':
        data=Product.objects.get(id=did)
        data.delete()
    else:
        raise Http404()
    return redirect('home')

def completed(request):
    data=order_product_detail.objects.filter(status='Delivered')
    d={'data':data,"allcat": allcat,}
    return render(request,'order.html',d)

def other(request):
    data=[]
    pending_order = order_product_detail.objects.all()
    for i in pending_order:
        if i.status != 'Delivered':
            data.append(i)
    d={'data':data,"allcat": allcat,'mycart':mycartdata(request.user)}
    return render(request,'pen.html',d)

def changestatus(request,idf):
    status = ['Order Confirmed','Shipped','Out for Delivery', 'Delivered']
    data=order_product_detail.objects.get(id=idf)
    ind=status.index(data.status)
    dropdown=status[ind+1:]
    if request.method == 'POST':
        s=request.POST['status']
        data.status=s
        data.save()
        return redirect('oth')
    d={"allcat": allcat,'mycart':mycartdata(request.user),'drop':dropdown,'da':data}
    return render(request,'chgstatus.html',d)
