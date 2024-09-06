from django.shortcuts import render,redirect
import pandas as pd
from userapp.models import userinfo
from django.db.models import Q
from django.http import HttpResponse
from openpyxl import Workbook

import datetime
datetime1=datetime.datetime.now()

def homepage(request):
    userdata = userinfo.objects.all()
    query1=request.GET.get('query')
    if query1:
        userdata=userinfo.objects.filter(

            Q(UName = query1) |
            Q(UType = query1) |
            Q(Status = query1) |
            Q(Email = query1)

        )
    return render(request,'homepage.html',{'userdata':userdata})


def userinfodata(request):
    if request.method == "GET":

        return render(request, 'userdata.html')
    else:
        userinfo(
            UID=request.POST.get('UID'),
            UName=request.POST.get('UName'),
            Password=request.POST.get('Password'),
            UType=request.POST.get('UType'),
            Status=request.POST.get('Status'),
            Mobile=request.POST.get('Mobile'),
            Email=request.POST.get('Email'),
            Cdatatime=datetime1
        ).save()

        return redirect('homepage')

def export_to_excel(request):
    userdata = userinfo.objects.all()
    columns= ["UID","UName","UType","Status","Mobile","Email","Cdatatime"]
    df=pd.DataFrame(list(userdata.values(*columns)))
    df['Cdatatime'] = df['Cdatatime'].dt.tz_localize(None)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=userdata.xlsx'
    with pd.ExcelWriter(response,engine='openpyxl')as writer:
        df.to_excel(writer,index=False,sheet_name='Sheet1')
    return response



