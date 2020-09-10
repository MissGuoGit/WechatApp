// pages/shopcar/shopcar.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        isshowpersoninfo:"none",
        btntxt:"去结算",
        carfoodlist:[],
        sumprice:0,
        date:'',
        sname:'',
        stel:'',
        ptime:'',
        saddress:'',
        memo:'',
        msg:""
      },
    //   自定义函数
    fntap:function(){
      var that=this;
      if(that.data.btntxt=="确定下单")
      {
        console.log("后面会执行下单操作")
        that.fnsaveorder();
      }
      else
      {
        that.setData({
          isshowpersoninfo:"block",
          btntxt:"确定下单"
        });
      }
  },
  // 下单操作开始
  fnsaveorder:function(){
    var that=this;
    var currentusertruename = wx.getStorageSync("currentusertruename");
    var currentuserid = wx.getStorageSync("currentuserid");
    console.log(currentusertruename);
    if(currentusertruename.length<1)
    {
        wx.showToast({
          title: '你还没有登录',
          icon:'none'
        });
        setTimeout(function(){
          wx.navigateTo({
            url: '/pages/login/login'
          });
        },2000);         
    }
    else
    {
      wx.request({
        url: 'http://localhost:8000/dcapi/saveorder',
        method: 'POST',
        data: {
          sumprice: that.data.sumprice,//总价
          sname: that.data.sname,
          stel: that.data.stel,
          saddress: that.data.saddress,
          ptime: that.data.ptime,
          memo: that.data.memo,
          userid: currentuserid,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc.data);
          wx.showToast({
            title: '下单成功!'
          });
          wx.redirectTo({
            url: '/pages/myorder/myorder',
          });
        }
      });

    } 
  },
  // 下单操作结束

    //购物车和订单页面的切换  
      fnback:function(){
        var that=this;
        that.setData({
          isshowpersoninfo:"none",
          btntxt:"去结算"
        });
      },

  // 获取订单表里面的数据然后保存在data中，方便传到后端
  bindDateChange:function(e){
    this.setData({
      ptime: e.detail.value
    });
  },
  fnsname:function(e){
    this.setData({
      sname: e.detail.value
    });
  },
  fntel:function(e){
    this.setData({
      stel: e.detail.value
    });
  },
  fnaddress: function (e) {
    this.setData({
      saddress: e.detail.value
    });
  },
  fnmemo: function (e) {
    this.setData({
      memo: e.detail.value
    });
  },
  // 获取订单内容结束


      // 购物车数量的加减
  fnjia:function(e){
    var id=e.currentTarget.dataset.id;
    this.fnchangenum(id,1);
  },
  fnjian:function(e){
    var id=e.currentTarget.dataset.id;
    this.fnchangenum(id,0);
  },
  fnchangenum:function(id,typeid)
  {
    var that=this;
    wx.request({
      url: 'http://localhost:8000/dcapi/changecarnum',
      method: 'POST',
      data: {
        id:id,
        typeid:typeid
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        that.fngetdata();
      }
    });
  },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
      var that=this;
      var currentuserid=wx.getStorageSync('currentuserid');
      console.log(currentuserid);
      if(currentuserid==undefined||currentuserid==null||currentuserid=="")
      {
        wx.navigateTo({
          url: '/pages/login/login',
        });
      }
      else
      {
        that.fngetdata();
      }
      
    },
    // 获取购物车中的数据
    fngetdata:function()
    {
      var that=this;
      var currentuserid=wx.getStorageSync('currentuserid');
      wx.request({
        url: 'http://localhost:8000/dcapi/getcarlist',
        method: 'POST',
        data: {
          userid :currentuserid
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc.data);
          var sum=0;
          cc.data.forEach(element => {
            sum+=parseFloat(element.price)*parseFloat(element.procount);
          });
          if(cc.data.length <=0){
            that.setData({
              msg:"亲，您的购物车空空如也，加入喜欢的菜品吧！"
            });
          }else{
            that.setData({
              msg:""
            });
          }
          that.setData({
            sumprice:sum,
            carfoodlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
            
          });
        }
      });
    },
    // 删除购物车里面的商品
    fndeleteitembyid:function(e){
      var that=this;
      var id=e.currentTarget.dataset.id;
      wx.request({
        url: 'http://localhost:8000/dcapi/deleteitembyid',
        method: 'POST',
        data: {
          id:id
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          that.fngetdata();
        }
      });
    },
    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})