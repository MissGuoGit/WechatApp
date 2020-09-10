// pages/test/test.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        length:0,
        flag:true,
        getdata:'',
        msg:""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    // 获取全局变量的实例
    onLoad: function (options) {
        const appInstance = getApp()
        console.log(appInstance.globalData.globalmsg) 
        //  调用getApp()函数来获取全局变量
    },
//   自定义函数
    clickfun:function(){
        var that = this;
        that.setData({
            getdata:'点击过后查询出来的数据'
        })
    },
    inputfun:function(e){
        console.log(e.detail.value);
        var that = this;
        that.setData({
            msg:e.detail.value
        })
    },
    savefun:function(){
        
    },
    jumpfun:function(){
    // 跳转方法一
    // wx.redirectTo({
    //   url: '/pages/foodview/foodview',
    //不能是tabBar的页面
    // })
    // 跳转方法二
    wx.navigateTo({
      url: '/pages/foodview/foodview',
    // 不能是tabBar的页面
    })
    // 跳转方法三
    // wx.switchTab({
    //   url: '/pages/index/index',
    // //  只能是tabBar的页面
    // })
    // wx.navigateBack({
    //  delta:1
    // })
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
// 小程序启动，或从后台进入前台显示时触发。
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {
// 小程序从前台进入后台时触发，简单点说就是切换下后台，暂时离开了小程序
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
  
    },
// 头像上传
    imgupload:function(){
        wx.chooseImage({
            count: 9, // 默认9
            sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
            sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
            success: function (res) {
            // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
            var tempFilePaths = res.tempFilePaths;
            wx.uploadFile({
            url: 'https://www.hgdqdev.cn/api/upload2',
            filePath: tempFilePaths[0],
            name: 'file',
            header: {
            'content-type': 'multipart/form-data'
            },
            success: function (res) {
            var data = res.data
            console.log(res);
            }
            })
            }
            })
    },



dianj:function(){
  wx.switchTab({
    url: '/pages/index/index',
  })

 },

})