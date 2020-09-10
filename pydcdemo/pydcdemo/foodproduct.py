from django.shortcuts import render, redirect #render是页面渲染
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
#引入数据库包
import pymysql
import datetime
import os
conn=pymysql.connect(
    user='root',
    password='123456',
    port=3306,
    host='127.0.0.1',
    db='myshop',
    charset='utf8'
)
cursor=conn.cursor()
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')

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

#请求添加页面
@xframe_options_exempt#允许跨域请求
def foodadd(request):
    return render(request, 'foodadd.html')


#增加菜品添加到数据库
@xframe_options_exempt
def foodaddpost(request):
    tbname = request.POST.get('tbname')
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')
    tbcontents = request.POST.get('tbcontents')

    fullname = ""
    # 图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):  # 有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]  # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束

    sqlstr = "insert into tbproduct (proname,price,brief,descriptions,imgurl,address,typeid) values ('" + tbname + "'," + tbprice + ",'" + tbbrief + "','" + tbcontents + "','" + fullname + "','重庆',1) "
    cursor.execute(sqlstr)
    print('插入成功')
    return render(request, 'foodadd.html')

#展示菜品列表
@xframe_options_exempt
def foodlist(request):
    strsql = "select id,proname,price,imgurl,brief from tbproduct order by id desc" #和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist=[]
    while row:
        #print(row)
        foodlist.append({"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"brief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html',{'foodlist': foodlist})

#修改列表中的菜品
@xframe_options_exempt
def foodedit(request):
    id = request.GET.get('id')
    strsql = "select id,proname,price,imgurl,brief,descriptions,address from tbproduct where id="+id  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    while row:
        # print(row)
        foodview={"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"brief": row[4],"descriptions": row[5],"address": row[6]}
        row = cursor.fetchone()
    return render(request, 'foodedit.html', {'foodview': foodview})


#修改列表中的菜品后提交
@xframe_options_exempt
def foodeditpost(request):
    proid = request.POST.get('proid')
    oldimgurl = request.POST.get('oldimgurl')
    tbname = request.POST.get('tbname')
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')
    tbcontents = request.POST.get('tbcontents')

    fullname = ""
    # 图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):  # 有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]  # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:  # 没有上传文件的情况
        fullname = oldimgurl
    # 图片上传结束

    sqlstr ="update tbproduct set proname='"+tbname+"',price="+tbprice+",brief='"+tbbrief+"',descriptions='"+tbcontents+"',imgurl='"+fullname+"' where id="+proid
    cursor.execute(sqlstr)
    view = {"id": proid, "proname": tbname, "price": tbprice, "imgurl": fullname, "brief": tbbrief,
            "descriptions": tbcontents,
            "address": ""}
    # script = "div = document.getElementsByClassName('msg')[0];submitbtn = document.getElementById('btnsave');submitbtn.onclick = function(){ div.setAttribute('class','msg show')}"
    # context = {}
    # context['sign'] = script

    #更新完成以后展示菜单列表
    strsql = "select id,proname,price,imgurl,brief from tbproduct order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist = []
    while row:
        # print(row)
        foodlist.append({"id": row[0], "proname": row[1], "price": row[2], "imgurl": row[3], "brief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html', {'foodlist': foodlist})
    #return render(request, 'foodedit.html', {'foodview': view},)#context
# {'script':script}

#删除列表中的菜品
def fooddelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from tbproduct where id="+id
    cursor.execute(sqlstr1)
    conn.commit()
    #重新查询数据，渲染列表模板
    sqlstr2 = "select id,proname,price,imgurl,brief from tbproduct order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist = []
    while row:
        # print(row)
        foodlist.append({"id": row[0], "proname": row[1], "price": row[2], "imgurl": row[3], "brief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html', {'foodlist': foodlist})

# 订单板块
#1、展示订单列表
@xframe_options_exempt
def orderlist(request):
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    list = []
    while row:
        # print(row)
        list.append(
            {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
             "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
        row = cursor.fetchone()
    return render(request, 'orderlist.html', {'list': list})
#2、删除订单
#注意只能先删除明细表再删除抬头表，不然因为约束关系报错
@xframe_options_exempt
def orderdelete(request):
   orderid = request.GET.get("orderid")
   strsql2 = "delete from tborderitems where orderid=" + orderid
   strsql1 = "delete from tborderhead where orderid=" + orderid
   cursor.execute(strsql2)
   cursor.execute(strsql1)
   #执行完删除以后，在将数据查询出来展示列表
   strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc"
   cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
   row = cursor.fetchone()
   list = []
   while row:
       # print(row)
       list.append(
           {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
            "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
       row = cursor.fetchone()
   return render(request, 'orderlist.html', {'list': list})
#3、订单详情
@xframe_options_exempt
def orderview(request):
    orderid = request.GET.get("orderid")
    strsqlitems = "select id,orderid,proid,proname,price,procount,imgurl from tborderitems where orderid='" + orderid + "'"
    strsqlhead = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead where orderid='" + orderid + "'"
    #查询详情表的内容
    cursor.execute(strsqlitems)
    rowitem = cursor.fetchone()
    list = []
    while rowitem:
        list.append(
            {"id": rowitem[0], "orderid": rowitem[1], "proid": rowitem[2], "proname": rowitem[3], "price": rowitem[4],
             "procount": rowitem[5],
             "imgurl": rowitem[6]})
        rowitem = cursor.fetchone()
    #查询抬头表的
    cursor.execute(strsqlhead)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    head = {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
            "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9], "items": list}

    return render(request, 'orderview.html', {'obj': head})
# 登录页面
@xframe_options_exempt#允许跨域请求
def login(request):
    return render(request, 'login.html')
# 登录
@xframe_options_exempt
def loginpost(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    strsql="select id,username,truename from tbusers where username='"+username+"' and password='"+password+"'"
    cursor.execute(strsql)
    row = cursor.fetchone()
    context = {}
    if row:
        #如果成功 就跳转到主页面
        return redirect("/static/myadmin/default.html")
    else:
        #重新渲染登录页面
        context['msg'] = '用户名或者密码错误!'
        return render(request, 'login.html', context)

# 轮播图页面
@xframe_options_exempt#允许跨域请求
def pptlist(request):
    strsql = "select id,imgurl from pptimg order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    pptlist = []
    while row:
        # print(row)
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    return render(request, 'pptlist.html', {'pptlist': pptlist})

#增加ppt图片添加到数据库和uploading
@xframe_options_exempt
def pptlistpost(request):

    fullname = ""
    # 图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):  # 有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]  # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束

    sqlstr = "insert into pptimg (imgurl) values ('" + fullname + "') "
    cursor.execute(sqlstr)
    print('插入成功')

    strsql = "select id,imgurl from pptimg order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    pptlist = []
    while row:
        # print(row)
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    return render(request, 'pptlist.html', {'pptlist': pptlist})
#删除列表中的菜品
@xframe_options_exempt
def pptdelete(request):
    id = request.GET.get('id')
    strsql1 = "delete from pptimg where id="+id
    cursor.execute(strsql1)
    #删除完成过后继续展示轮播列表
    strsql = "select id,imgurl from pptimg order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    pptlist = []
    while row:
        # print(row)
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    return render(request, 'pptlist.html', {'pptlist': pptlist})
