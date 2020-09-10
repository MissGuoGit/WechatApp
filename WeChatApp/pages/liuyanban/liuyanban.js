// pages/liuyanban/liuyanban.js
// 加载当前的时间：
var util = require("../../utils/util.js");


Page({

    /**
     * 页面的初始数据
     */
    data: {
     sendtime:"",
     msglist:[],
     username:"",
     tel:"",
     msgcontain:"",
     hidden:"true"

    },
// 写留言的点击事件
addmessage:function(e){
    // console.log("-------")
    this.setData({
      hidden:""
    })
  },
// 取消发布留言点击
  notsend:function(){
    // console.log("-------")
    this.setData({
      hidden:"ture"
    })
  },

// 获取输入评论区的内容存到data
getcontain:function(e){
    // console.log(e.detail.value)
    this.setData({
        msgcontain:e.detail.value
    })
},
// 点击发送获取当前时间并将数据提交到后端
sendmessage:function(){
    var that = this
    var currenttime = util.formatTime(new Date());
    this.setData({
        sendtime: currenttime,
        });
    var sendtime = that.data.sendtime;
    console.log(sendtime)
    var msgcontain = that.data.msgcontain;
    var currentusername=wx.getStorageSync('currentusername');
    var currentuserimg=wx.getStorageSync('currentuserimg');
    wx.request({
        url: 'http://localhost:8000/dcapi/addmsg',
        method: 'POST',
        data: {
            sendtime:sendtime,
            msgcontain:msgcontain,
            currentusername:currentusername,
            currentuserimg:currentuserimg
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc.data);
          that.setData({
            hidden:"true",
            msglist:cc.data,//把后端查询出来的菜品列表信息存放到foodlist数组中
            msgcontain:""
           });
          wx.showToast({
            title: '发布成功',
          })

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
    // 一开始加载出评论页面
    onShow: function () {
        var that=this; 
        wx.request({
          url: 'http://localhost:8000/dcapi/getlistmsg',
          method: 'POST',
          data: {
            
          },
          header: {
            'content-type': 'application/x-www-form-urlencoded' // 默认值
          },
          dataType: 'json',
          success(cc) {
            console.log(cc.data);
            that.setData({
             msglist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
            });
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