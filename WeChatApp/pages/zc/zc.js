// pages/zc/zc.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      username:"",
      password:"",
      repassword:"",
      phonenumber:"",
      address:"",
      truename:"",
      msg:"",
      imgurlbase:""
    },
    // 获取input里面的数据值
    fninputeditusername:function(e){
      var that=this;
      // console.log(e.detail.value);
      that.setData({
        username:e.detail.value
      });
  
  },
  fninputeditpassword:function(e){
    var that=this;
    // console.log(e.detail.value);
    that.setData({
      password:e.detail.value
    });
  
  },
  fninputeditrepassword:function(e){
    var that=this;
    var repassword = e.detail.value;
       that.setData({
        repassword:repassword
       })
    },
  fninputedittel:function(e){
      var that=this;
      // console.log(e.detail.value);
      that.setData({
        phonenumber:e.detail.value
      });
    
    },
  fninputeditadd:function(e){
    var that=this;
    // console.log(e.detail.value);
    that.setData({
      address:e.detail.value
    });
  
  },
  fninputedittruename:function(e){
    var that=this;
    // console.log(e.detail.value);
    that.setData({
      truename:e.detail.value
    });
  
  },
    
   // 获取input里面的数据值结束 
  fnzhuce:function(){
    var that = this;
    var password = that.data.password;
    var repassword = that.data.repassword;
    var username = that.data.username;
    var phonenumber = that.data.phonenumber;
    var address = that.data.address;
    var truename = that.data.truename;
    if(!username.length>0)
    {
      wx.showToast({
        title: '请输入账号!',
        icon:'none'
      });
      return;
    }
   
   if(!password.length>0)
    {
      wx.showToast({
        title: '请输入密码!',
        icon:'none'
      });
      return;
    }
    if(!phonenumber.length>0)
    {
      wx.showToast({
        title: '请输入手机号码!',
        icon:'none'
      });
      return;
    }
    if(!address.length>0)
    {
      wx.showToast({
        title: '请输入地址!',
        icon:'none'
      });
      return;
    }
    if(!truename.length>0)
    {
      wx.showToast({
        title: '请输入真实姓名!',
        icon:'none'
      });
      return;
    }
    if (password!=repassword) {
      that.setData({
        repassword:"",
        msg:""
       });
       wx.showToast({
         title: '两次密码不一致',
         icon:'none'
       });
      console.log("密码不一致")
    }
    else{
      that.fnsendzhuce();
    }
   
  
  },
// 上传头像
//wx.chooseImage：得到图片地址 
// wx.getFileSystemManager：创建文件管理类 
// readFileSync：读取本地文件，直接得到base64
fngetimg:function(){
  var that = this;
    wx.chooseImage({
      // complete: (res) => {/pages/},//不管成功与否执行的代码
      success(res){
        console.log(11111)
        var baseimg = wx.getFileSystemManager().readFileSync(res.tempFilePaths[0], "base64");
        that.setData({
          imgurlbase:"data:image/png;base64,"+baseimg 
        })
        wx.showToast({
          title: '头像上传成功'
        });
      }
    }) 
  },
  // 发起一个请求，保存到数据库
    fnsendzhuce:function(){
      var that=this;
      var username= this.data.username;
      var password=this.data.password;
      var phonenumber=this.data.phonenumber;
      var address = that.data.address;
      var truename = that.data.truename;
      var imgurlbase = that.data.imgurlbase;
      // console.log(username);
      // console.log(password);
  
      wx.request({
        url: 'http://localhost:8000/dcapi/zhuce',
        method: 'POST',
        data: {
          username: username,
          password: password,
          phonenumber:phonenumber,
          address:address,
          imgurlbase:imgurlbase,
          truename:truename
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
           console.log(cc.data);
          if(cc.data.length<=0)
          {
            // console.log(cc.data[0].truename);
            // wx.setStorageSync("username","tangyan")
            wx.showToast({
              title: '注册成功'
            });
            setTimeout(function () {
                wx.navigateTo({
                  url: '/pages/login/login',
                })
            }, 1000);
            that.setData({
              msg: ""
            });
             }
          else
             {
            that.setData({
              msg: "提示：该用户已注册！"
            });
          }
          
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
  