// pages/foodview/foodview.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      foodprice:'',//菜品的单价
      buynum:1,//订购的数量
      sumprice:'',//总价
      proname:'',
      brief:'',
      descriptions:'',
      imgurl:'',
      foodid:''
  
    },
    fnsaveorder:function () {
     wx.switchTab({
       url: '/pages/shopcar/shopcar',
     })  
    },
    /**
     * 生命周期函数--监听页面加载
     */
    // 获取到对应id的菜品详情
    onLoad: function (options) {
      var that=this;
      var id = options.id;
      console.log(id);
      that.setData({
        foodid:id
      });
      wx.request({
        url: 'http://localhost:8000/dcapi/getfoodbyid',
        method: 'POST',
        data: {
          id: id
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc.data);
          that.setData({
            foodprice:cc.data[0].price,
            sumprice:cc.data[0].price,
            proname: cc.data[0].proname,
            brief: cc.data[0].brief,
            descriptions: cc.data[0].descriptions,
            imgurl:"http://localhost:8000/static/uploadimg/"+cc.data[0].imgurl
          });
        }
      });
    },
    fnjia:function(){
      var price = this.data.foodprice;
      var buynum = this.data.buynum;
      // console.log(price);
      var newnum = buynum+1;
      // console.log(newnum);
      this.setData({
        buynum:newnum,
        sumprice:newnum * price
      })
     

    },
    fnjian:function(){
      var price = this.data.foodprice;
      var buynum = this.data.buynum;
      // console.log(price);
      var newnum = buynum-1;
      // console.log(newnum);
      if (newnum<1) {
        newnum = 1;
      }
      this.setData({
        buynum:newnum,
        sumprice:newnum * price
      })
    },
    // 加入购物车功能
    fnaddtocar:function(){
      var that=this;
      //wx.setStorageSync("currentuserid", cc.data[0].id);
      var currentuserid=wx.getStorageSync('currentuserid');
      if(currentuserid>0)
      {
          //如果登录了，就加入购物车
        var proid=that.data.foodid;
        var proname=that.data.proname;
        var procount=that.data.buynum;
        var imgurl=that.data.imgurl;
        var price=that.data.foodprice;
        wx.request({
          url: 'http://localhost:8000/dcapi/addtocar',
          method: 'POST',
          data: {
            userid: currentuserid,
            proid:proid,
            proname:proname,
            procount:procount,
            imgurl:imgurl,
            price:price
          },
          header: {
            'content-type': 'application/x-www-form-urlencoded' // 默认值
          },
          dataType: 'json',
          success(cc) {
            console.log(cc.data);
            wx.switchTab({
              url: '/pages/shopcar/shopcar'
            });
          }
        });
  
      }
      else
      {
        wx.navigateTo({
          url: '/pages/login/login',
        })
      }
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