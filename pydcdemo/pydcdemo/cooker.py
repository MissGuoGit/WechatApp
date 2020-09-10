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

#请求添加页面
@xframe_options_exempt#允许跨域请求
def cookeradd(request):
    return render(request, 'cookeradd.html')


#增加厨师添加到数据库  select id,cookername,cookerlevel,imgurl,specialfood,cookerbreif
@xframe_options_exempt
def cookeraddpost(request):
    cookername = request.POST.get('cookername')
    cookerlevel = request.POST.get('cookerlevel')
    specialfood = request.POST.get('specialfood')
    cookerbreif = request.POST.get('cookerbreif')

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

    sqlstr = "insert into cooker (cookername,cookerlevel,specialfood,cookerbreif,imgurl) values ('" + cookername + "','" + cookerlevel + "','" + specialfood + "','" + cookerbreif + "','" + fullname + "') "
    cursor.execute(sqlstr)
    print('插入成功')
    return render(request, 'cookeradd.html')

#展示菜品列表
@xframe_options_exempt
def cookerlist(request):
    strsql = "select id,cookername,cookerlevel,imgurl,specialfood,cookerbreif from cooker order by id desc" #和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    cookerlist=[]
    while row:
        #print(row)
        cookerlist.append({"id": row[0], "cookername": row[1], "cookerlevel": row[2],"imgurl": row[3],"specialfood": row[4],"cookerbreif": row[5]})
        row = cursor.fetchone()
    return render(request, 'cookerlist.html',{'cookerlist': cookerlist})

#修改列表中的厨师
@xframe_options_exempt
def cookeredit(request):
    id = request.GET.get('id')
    strsql = "select id,cookername,cookerlevel,imgurl,specialfood,cookerbreif from cooker where id="+id  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    while row:
        # print(row)
        cookerview={"id": row[0], "cookername": row[1], "cookerlevel": row[2],"imgurl": row[3],"specialfood": row[4],"cookerbreif": row[5]}
        row = cursor.fetchone()
    return render(request, 'cookeredit.html', {'cookerview': cookerview})


#修改列表中的厨师后提交
@xframe_options_exempt
def cookereditpost(request):
    proid = request.POST.get('proid')
    oldimgurl = request.POST.get('oldimgurl')
    cookername = request.POST.get('cookername')
    cookerlevel = request.POST.get('cookerlevel')
    specialfood = request.POST.get('specialfood')
    cookerbreif = request.POST.get('cookerbreif')

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

    sqlstr ="update cooker set cookername='"+cookername+"',cookerlevel='"+cookerlevel+"',specialfood='"+specialfood+"',cookerbreif='"+cookerbreif+"',imgurl='"+fullname+"' where id='"+proid+"'"
    cursor.execute(sqlstr)
    view = {"id": proid, "cookername": cookername, "cookerlevel": cookerlevel, "imgurl": fullname, "specialfood": specialfood,
            "cookerbreif": cookerbreif}
    # script = "div = document.getElementsByClassName('msg')[0];submitbtn = document.getElementById('btnsave');submitbtn.onclick = function(){ div.setAttribute('class','msg show')}"
    # context = {}
    # context['sign'] = script

    #更新完成以后展示厨师列表
    strsql = "select id,cookername,cookerlevel,imgurl,specialfood,cookerbreif from cooker order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    cookerlist = []
    while row:
        # print(row)
        cookerlist.append(
            {"id": row[0], "cookername": row[1], "cookerlevel": row[2], "imgurl": row[3], "specialfood": row[4],
             "cookerbreif": row[5]})
        row = cursor.fetchone()
    return render(request, 'cookerlist.html', {'cookerlist': cookerlist})
    #return render(request, 'foodedit.html', {'foodview': view},)#context
# {'script':script}

#删除列表中的厨师
@xframe_options_exempt
def cookerdelete(request):
    id = request.GET.get('id')
    strsql1 = "delete from cooker where id="+id
    cursor.execute(strsql1)
    #删除完成过后继续展示菜品列表
    strsql2 = "select id,cookername,cookerlevel,imgurl,specialfood,cookerbreif from cooker order by id desc"  # 和下面对应索引，最好不查询*
    cursor.execute(strsql2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    cookerlist = []
    while row:
        # print(row)
        cookerlist.append(
            {"id": row[0], "cookername": row[1], "cookerlevel": row[2], "imgurl": row[3], "specialfood": row[4],
             "cookerbreif": row[5]})
        row = cursor.fetchone()
    return render(request, 'cookerlist.html', {'cookerlist': cookerlist})
