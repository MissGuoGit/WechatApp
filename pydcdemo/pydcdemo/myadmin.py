from django.shortcuts import render, redirect #render是页面渲染
from django.http import HttpResponse

def test(request):
    return render(request, 'test.html')

def testdata(request):
    context = {}
    context['sign'] = '数据传输测试!'#hello是指一个属性标记，
    return render(request, 'testdata.html',context)

def hello(request):
    s="<h1 style='color:green;'>welcome to rongzhi</h1>"
    response = HttpResponse(s)
    #允许跨域使用
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response