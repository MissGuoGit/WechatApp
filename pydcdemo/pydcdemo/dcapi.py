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
@xframe_options_exempt
def login(request):
    #print("接收到的参数typeid="+str(request.GET.get("typeid")))
    username=request.POST.get("username")
    password = request.POST.get("password")
    print(username)
    print(password)
    strsql="select id,username,password,truename,tel,address,imgurlbase from tbusers where username='"+username+"' and password='"+password+"' "
    cursor.execute(strsql)
    conn.commit()
    row = cursor.fetchone()
    s=""
    if row:
        s=str({"id": row[0], "username": row[1], "password": row[2], "truename": row[3], "tel": row[4], "address": row[5],"imgurlbase": row[6]})
        s=s.replace("'","\"")
    res="["+s+"]"
    # 以json数据格式返回
    response=HttpResponse(res)
    #允许跨域请求
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    #返回json格式的数据
    return response
# 注册功能
def zhuce(request):
    username=request.POST.get("username")
    password = request.POST.get("password")
    tel = request.POST.get("phonenumber")
    address = request.POST.get("address")
    imgurlbase = request.POST.get("imgurlbase")
    truename = request.POST.get("truename")
    #strsql = "insert into tbusers (username,password,truename,tel,address) values ('"+username+"','"+password+"','"+truename+"','"+tel+"','"+address+"')";
    # cursor.execute(strsql)
    strsql = "select id,username,password,truename,tel,address from tbusers where username='" + username+"'"
    cursor.execute(strsql)
    conn.commit()
    row = cursor.fetchone()
    s = ""
    if row:
        s = str({"id": row[0], "username": row[1], "password": row[2], "truename": row[3], "tel": row[4],
                 "address": row[5]})
        s = s.replace("'", "\"")
        res = "[" + s + "]"
    else:
        cursor.execute('insert into tbusers (username,password,truename,tel,address,imgurlbase) value (%s,%s,%s,%s,%s,%s)',(username,password,truename,tel,address,imgurlbase))
        conn.commit()
        s=""
        res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 首页随机菜单列表
@xframe_options_exempt
def getfoodlistbyrandom(request):
    strsql1 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by  RAND() limit 4 "
    cursor.execute(strsql1)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


# 首页随机厨师列表
@xframe_options_exempt
def getcookerlistbyrandom(request):
    strsql2 = "select id,cookername,cookerlevel,imgurl from cooker order by  RAND() limit 3 "
    cursor.execute(strsql2)
    conn.commit()
    cookerlist = []
    row = cursor.fetchone()
    while row:
        cookerlist.append({"id": row[0], "cookername": row[1], "cookerlevel":str(row[2]), "imgurl": row[3]})
        row = cursor.fetchone()
    c = str(cookerlist)
    c = c.replace("'", "\"")
    response = HttpResponse(c)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


# 首页随机轮播列表
@xframe_options_exempt
def getpptlistbyrandom(request):
    strsql3 = "select id,imgurl from pptimg order by  RAND() limit 3 "
    cursor.execute(strsql3)
    conn.commit()
    pptlist = []
    row = cursor.fetchone()
    while row:
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    p = str(pptlist)
    p = p.replace("'", "\"")
    response = HttpResponse(p)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response



@xframe_options_exempt
def getfoodbyid(request):
    id= request.POST.get("id")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where id="+id
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    if row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
#  查询菜单列表，并且实现相对应的查询功能
@xframe_options_exempt
def getfoodlist(request):
    key= request.POST.get("key")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by id desc "
    # key.strip()是指去掉空格无效字符
    if not key.strip()=="":
        strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where proname like '%"+key+"%'  order by id desc "#like后面的为模糊查询
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 加入购物车功能
@xframe_options_exempt
def addtocar(request):
    userid = request.POST.get('userid')
    proid = request.POST.get('proid')
    proname = request.POST.get('proname')
    procount = request.POST.get('procount')
    imgurl = request.POST.get('imgurl')
    price = request.POST.get('price')
    ctime = datetime.datetime.now().strftime('%F %T')
    # 加入购物车的时候先检查是不是同一个人的同样的菜品，如果是就更新，不是就插入数据
    strsql1 = "select id from tbshoppingcar where proid=" + proid+ " and sessionid=" +userid
    cursor.execute(strsql1)
    conn.commit()
    row = cursor.fetchone()
    strsql2 = "insert into tbshoppingcar(sessionid,proname,proid,procount,ctime,imgurl,price) values (" + userid + ",'" + proname + "'," + proid + "," + procount + ",'" + ctime + "','" + imgurl + "'," + price + ") "
    if row:
        strsql2 = "update tbshoppingcar set procount=procount+" + procount + " where proid=" + proid+" and sessionid=" +userid
    print(strsql2)
    cursor.execute(strsql2)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 加载购物车列表
@xframe_options_exempt
def getcarlist(request):
    userid= request.POST.get("userid")
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "sessionid": row[1], "proname":row[2], "proid": row[3], "procount": row[4],"ctime": row[5],"imgurl": row[6],"price":str(row[7])})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 改变购物车菜品数量
@xframe_options_exempt
def changecarnum(request):
    id= request.POST.get("id")
    typeid = request.POST.get("typeid")
    strsql = "update tbshoppingcar set procount=procount+1 where id=" + id
    if typeid=="0":
        strsql = "update tbshoppingcar set procount = IF(procount > 1, procount - 1,1) where id=" + id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 删除购物车已有菜品
@xframe_options_exempt
def deleteitembyid(request):
    id= request.POST.get("id")
    strsql = "delete from tbshoppingcar where id="+id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 购物车菜品下单
@xframe_options_exempt
def saveorder(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    orderid = datetime.datetime.strftime(t, "%Y%m%d%H%M%S%f")
    userid= request.POST.get("userid")
    sumprice = request.POST.get("sumprice")
    sname = request.POST.get("sname")
    stel = request.POST.get("stel")
    saddress = request.POST.get("saddress")
    ptime = request.POST.get("ptime")
    memo = request.POST.get("memo")
    #插入表头信息,注意如果是数字直接就是双引号，字符串就要单引号加双引号的衔接
    cursor.execute("insert into tborderhead (orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo) values ('"+orderid+"','"+sname+"','"+stel+"','"+saddress+"',"+sumprice+","+userid+",'"+ctime+"','"+ptime+"','"+memo+"')")
    conn.commit()

    #把购物车里面的数据插入到订单明细表
    #先把购物车里当前这个人的菜品查询出来
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    #构造插入订单明细表的sql语句
    sqllists = []
    row = cursor.fetchone()
    while row:
        #{"id": row[0], "sessionid": row[1], "proname": row[2], "proid": row[3], "procount": row[4], "ctime": row[5],"imgurl": row[6], "price": str(row[7])}
        sqllists.append("insert into tborderitems (orderid,proid,proname,price,procount,imgurl) values ('"+orderid+"',"+str(row[3])+",'"+row[2]+"',"+str(row[7])+","+str(row[4])+",'"+row[6]+"')")
        row = cursor.fetchone()
    #遍历sql列表，执行插入订单明细表操作
    for sqlitem in sqllists:
        cursor.execute(sqlitem)
        conn.commit()
    #清空购物车
    cursor.execute("delete from tbshoppingcar where sessionid="+userid)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

#加载订单列表
@xframe_options_exempt
def getorderlist(request):
    userid = request.POST.get("userid")
    strsql = "select id,orderid,proname,price,procount,imgurl,sname,stel,saddress,ctime,ptime,memo from v_order where memberid=" + userid
    cursor.execute(strsql)
    conn.commit()
    orderlist = []
    row = cursor.fetchone()
    while row:
        orderlist.append(
            {"id": row[0], "orderid": row[1], "proname": row[2], "price":str(row[3]), "procount": row[4], "imgurl": row[5],
             "sname": row[6], "stel": str(row[7]), "saddress": str(row[8]), "ctime": str(row[9]), "ptime": str(row[10]),"memo": str(row[11])})
        row = cursor.fetchone()
    s = str(orderlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 查询厨师的列表信息
#getcookerlist
@xframe_options_exempt
def getcookerlist(request):
    key= request.POST.get("key")
    strsql = "select id,cookername,cookerlevel,cookerbreif,specialfood,imgurl from cooker order by id desc "
    # key.strip()是指去掉空格无效字符
    if not key.strip()=="":
        strsql = "select id,cookername,cookerlevel,cookerbreif,specialfood,imgurl from cooker where cookername like '%"+key+"%'  order by id desc "#like后面的为模糊查询
    cursor.execute(strsql)
    conn.commit()
    cookerlist = []
    row = cursor.fetchone()
    while row:
        cookerlist.append({"id": row[0], "cookername": row[1], "cookerlevel":str(row[2]), "cookerbreif": row[3], "specialfood": row[4],"imgurl": row[5]})
        row = cursor.fetchone()
    s = str(cookerlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 查询厨师的对应详情
@xframe_options_exempt
def getcookerbyid(request):
    id= request.POST.get("id")
    # 查询厨师的基本信息
    strsql = "select id,cookername,cookerlevel,cookerbreif,specialfood,imgurl from cooker where id="+id
    cursor.execute(strsql)
    conn.commit()
    cookerlist = []
    row = cursor.fetchone()
    if row:
        cookerlist.append({"id": row[0], "cookername": row[1], "cookerlevel":str(row[2]), "cookerbreif": row[3], "specialfood": row[4],"imgurl": row[5]})
    s = str(cookerlist)
    s = s.replace("'", "\"")
    # 查询厨师对应的拿手菜
    strsq2 = "select id,proname,price,brief,imgurl from v_cookerhasproduct where id=" + id
    cursor.execute(strsq2)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price": str(row[2]), "brief": row[3],"imgurl": row[4]})
        row = cursor.fetchone()
    # if row:
    #     foodlist.append({"id": row[0], "proname": row[1], "brief": str(row[2]), "imgurl": row[3]})
    f = str(foodlist)
    f = f.replace("'", "\"")
    # 将两部分数据合在一起，还是以json格式返回
    res="[{\"cookerlist\":"+s+",\"foodlist\":"+f+"}]"

    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

# 留言板功能模块
# 获取留言板列表信息
@xframe_options_exempt
def getlistmsg(request):
    strsql = "select id,username,userimg,currenttime,msgcontain from messageboard order by id desc "
    # key.strip()是指去掉空格无效字符
    cursor.execute(strsql)
    conn.commit()
    messagelist = []
    row = cursor.fetchone()
    while row:
        messagelist.append({"id": row[0], "username": row[1], "userimg":str(row[2]), "currenttime": row[3], "msgcontain": row[4]})
        row = cursor.fetchone()
    s = str(messagelist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
# 新增留言
@xframe_options_exempt
def addmsg(request):
    currentusername = request.POST.get('currentusername')
    currentuserimg = request.POST.get('currentuserimg')
    sendtime = request.POST.get('sendtime')
    msgcontain = request.POST.get('msgcontain')
    # print(currentuserimg)
    sqlstr = "insert into messageboard (username,userimg,currenttime,msgcontain) values ('" + currentusername + "','"+currentuserimg+"','" + sendtime + "','" + msgcontain + "') "
    cursor.execute(sqlstr)
    conn.commit()
    # 新增完以后在查询
    strsql2 = "select id,username,userimg,currenttime,msgcontain from messageboard order by id desc "
    # key.strip()是指去掉空格无效字符
    cursor.execute(strsql2)
    conn.commit()
    messagelist = []
    row = cursor.fetchone()
    while row:
        messagelist.append({"id": row[0], "username": row[1], "userimg":str(row[2]), "currenttime": row[3], "msgcontain": row[4]})
        row = cursor.fetchone()
    s = str(messagelist)
    s = s.replace("'", "\"")
    # s = "{\"msg\":\"ok\"}"是否插入成功
    # res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response