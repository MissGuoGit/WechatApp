// pages/myorder/myorder.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        orderlist:[]
    },

// 订单详情页面获取订单表里面的数据

onLoad: function (options) {
    var that=this;
    // var currentusertruename = wx.getStorageSync("currentusertruename");
    var currentuserid = wx.getStorageSync("currentuserid");
    wx.request({
      url: 'http://localhost:8000/dcapi/getorderlist',
      method: 'POST',
      data: {
        userid:currentuserid 
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
            orderlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
            
          });
      }
    });
  },

    /**
     * 生命周期函数--监听页面初次渲染完成
     * id,orderid,proname,price,procount,imgurl,sname,stel,saddress,ctime,ptime,memo
     */
    onReady: function () {

    },


    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

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