// pages/foodlist/foodlist.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    foodlist:[],
    key:''
  },
  fnsearchinputchange:function(e){
    var that = this;
    var curvalue = e.detail.value;
    getApp().globalData.key=curvalue;
    this.fngetdata();
  },
  fngotofoodview:function(e){
    console.log(e.currentTarget.dataset.id);
    
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+e.currentTarget.dataset.id,
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
  onShow:function(){
    var v=getApp().globalData.key;
    console.log(v);
    this.setData({
      key:v
    });
    this.fngetdata();
  },

  
  fngetdata:function()
  {
    var that=this;
    var key=getApp().globalData.key;
    if(key==undefined||key==null)
    {
      key="";
    }
    wx.request({
      url: 'http://localhost:8000/dcapi/getfoodlist',
      method: 'POST',
      data: {
        key:key
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          foodlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
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