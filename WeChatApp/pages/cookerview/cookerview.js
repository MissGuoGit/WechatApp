// pages/cookerview/cookerview.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      cookername:"",
      cookerlevel:"",
      specialfood:"",
      cookerbreif:"",
      imgurl:"",
      foodlist:[],
      cookerlist:[]
    },

    /**
     * 生命周期函数--监听页面加载
     */
    fngotofoodview:function(e){
      console.log(e.currentTarget.dataset.id);
      
        wx.navigateTo({
          url: '/pages/foodview/foodview?id='+e.currentTarget.dataset.id,
        });
    },
    gotofoodlist:function(){
        wx.switchTab({
          url: '/pages/foodlist/foodlist',
        })
    },
    // 获取到对应id的厨师详情
    onLoad: function (options) {
        var that=this;
        var id = options.id;
        console.log(id);
        that.setData({
          cookerid:id
        });
        wx.request({
          url: 'http://localhost:8000/dcapi/getcookerbyid',
          method: 'POST',
          data: {
            id: id
          },
          header: {
            'content-type': 'application/x-www-form-urlencoded' // 默认值
          },
          dataType: 'json',
          success(cc) {
            console.log(cc.data)
            var cookerlist = cc.data[0].cookerlist;
            var foodlist = cc.data[0].foodlist;
            console.log(cookerlist[0].cookername);
            that.setData({
              cookername:cookerlist[0].cookername,
              cookerlevel:cookerlist[0].cookerlevel,
              specialfood: cookerlist[0].specialfood,
              cookerbreif: cookerlist[0].cookerbreif,
              imgurl:"http://localhost:8000/static/uploadimg/"+cookerlist[0].imgurl,
            
                // cookerlist:cc.data[0].cookerlist,//把后端查询出来的菜品列表信息存放到foodlist数组中
              foodlist:foodlist
             
            });
          }
        });
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