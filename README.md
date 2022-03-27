# NCUAutomaticSignInForWeChat
 这个脚本主要是为了南昌大学企业微信号的健康打卡，其实代码很简单。除了打卡外，还带有邮件提醒，如果打卡失败会再尝试3次，每次间隔20分钟，期间打卡成功自动停止，3次还没打成也结束。
1. 这个脚本事实上不是完善的脚本，需要一定的前提，我搞了一天多时间不想搞了浪费时间，反正能打卡就行了。目前这个脚本挂在云服务器上。
2. 使用这个脚本首先你得学会抓包，里面的参数值只有抓包才能看到并填写成自己的数据。其次，设置好自己的邮箱，不会的百度脚本中导入的邮箱模块
3. 需要填写成自己的参数数据有：  
   （1）token  
   （2）ncu_rygk_work_weixin_token这个值跟token值是一样的  
   （3）ncu_rygk_work_weixin_userData  
   （4）msg_from写邮箱地址  
   （5）msg_to写成跟（4）中一样的地址  
   （6）password邮箱通行码  
   （7）userId你自己的学号  
   （8）addressInfo你自己的地址，也就是企业微信号每日健康打卡中的详细地址一栏  
4.全部纯手撸的，半天时间搞定，凑合用把（反正我是能用）
![](https://github.com/anjing66/NCUAutomaticSignInForWeChat/blob/main/%E7%A4%BA%E6%84%8F%E5%9B%BE.jpg)

   
   
