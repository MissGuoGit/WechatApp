// pages/login/login.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        username: '',
        password: '',
        msg:''
    },
    fninputeditusername:function(e){
    // console.log(e.detail.value)
     var that = this;
     that.setData({
     username:e.detail.value
     })
    },
    fninputeditpassword:function(e){
        // console.log(e.detail.value)
        var that = this;
        that.setData({
        password:e.detail.value
        })
    },
    fnlogin:function(){
        var that = this;
    wx.request({
      url: 'http://localhost:8000/dcapi/login',
      method: 'POST',
      data: {
        username: that.data.username,
        password: that.data.password,
        csrfmiddlewaretoken:'',
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        if(cc.data.length>0)
        {
          console.log(cc.data[0].username);//undefined一般是数据格式的问题
          console.log(11111)
          wx.setStorageSync("currentuserid", cc.data[0].id);
          wx.setStorageSync("currentusername",cc.data[0].username);
          wx.setStorageSync("currentusertruename", cc.data[0].truename);
          wx.setStorageSync("currentusertruetel", cc.data[0].tel);
          wx.setStorageSync("currentusertrueaddress", cc.data[0].address);
          wx.setStorageSync("currentuserimg", cc.data[0].imgurlbase);
          wx.showToast({
            title: '登录成功'
          });
          setTimeout(function () {
              wx.switchTab({
                url: '/pages/index/index',
              })
          }, 1000);
          that.setData({
            msg: ""
          });
        }
        else
        {
          that.setData({
            msg:"用户名或密码错误"
          });
        }
        
      }
    });

    },
    // 跳转到注册
    fngotoreg:function(){
      wx.navigateTo({
        url: '/pages/zc/zc',
      })
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