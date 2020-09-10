//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    foodlist:[],
    cookerlist:[],
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数a
  cooker:function(){
    wx.navigateTo({
      url: '/pages/cooker/cooker',
    })
  },
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  fnedit:function(e){
   var currentvalue = e.detail.value;
  //  console.log(currentvalue);
  getApp().globalData.key = currentvalue;
  },
  fnsearch(){
  wx.switchTab({
    url: '/pages/foodlist/foodlist',
  })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  // 在后台随机加载四个菜品
  onShow:function(){
     this.fngetpptlistbyrandom();
     
     
//  请求cookerlist随机
   
  },
  //在此处编写请求首页菜品数据的函数
  fngetfoodlistbyrandom:function(){
    var that=this; 
    wx.request({
      url: 'http://localhost:8000/dcapi/getfoodlistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(ff) {
        // console.log(typeof ff.data);
        that.setData({
          foodlist:ff.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
        that.fngetcookerlistbyrandom();
      }
    });
  },
  // 获取随机的厨师名单
  fngetcookerlistbyrandom:function(){
    var that = this;
    wx.request({
      url: 'http://localhost:8000/dcapi/getcookerlistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        // console.log(typeof cc.data);
        that.setData({
          cookerlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
      }
    });
  },
    //在此处编写请求首页菜品数据的函数
    fngetpptlistbyrandom:function(){
      var that=this; 
      wx.request({
        url: 'http://localhost:8000/dcapi/getpptlistbyrandom',
        method: 'POST',
        data: {
          
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(pp) {
          // console.log(pp.data);
          that.setData({
            pptlist:pp.data//把后端查询出来的菜品列表信息存放到foodlist数组中
          });
          that.fngetfoodlistbyrandom()
          
        }
      });
    },
  // 从列表菜品到对应的详情
  fngotofoodview:function(e){
    console.log(e.currentTarget.dataset.id);
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+e.currentTarget.dataset.id,
      });
  },
  fngotocookerview:function(e){
    console.log(e.currentTarget.dataset.id);
      wx.navigateTo({
        url: '/pages/cookerview/cookerview?id='+e.currentTarget.dataset.id,
      });
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  // 页面的跳转
  gotofoodlist:function(){
    wx.switchTab({
      url:"/pages/foodlist/foodlist"
    })
  },
  gotocookerlist:function(){
    wx.navigateTo({
      url:"/pages/cooker/cooker"
    })
  },
  // 获取订单页面
  gotoorderlist:function(){
    var that=this;
      var currentusertruename=wx.getStorageSync('currentusertruename');
      console.log(currentusertruename);
      if(currentusertruename==undefined||currentusertruename==null||currentusertruename=="")
      {
        wx.redirectTo({
          url: '/pages/login/login',
        });
      }
      else
      {
        wx.navigateTo({
          url:"/pages/myorder/myorder"
        })
      }
   
  },


})
