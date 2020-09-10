// pages/myself/myself.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
     username:"",
     userimg:""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    // 自定义函数
    fngotomyorder:function(){
       wx.navigateTo({
         url: '/pages/myorder/myorder',
       }) 
    },
    fngotomessage:function(){
      wx.navigateTo({
        url: '/pages/liuyanban/liuyanban',
      }) 
    },
    // 取出本地的数据
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
        that.fngetdata();
      }
      
    },
    fngetdata:function(){
      var that=this;
     
      var currentusername=wx.getStorageSync('currentusername');
      var currentuserimg=wx.getStorageSync('currentuserimg');
      // console.log()
      console.log(currentusername)
      that.setData({
        username:currentusername,
        userimg:currentuserimg
      })
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