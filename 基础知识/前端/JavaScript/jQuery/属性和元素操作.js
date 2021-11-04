$(function (){
    //属性操作
    //获取元素的属性，attr()方法需要一个参数——属性名
    var href = $('.div1 a').eq(0).attr('href');
    console.log(href)

    //写入属性，attr()方法需要两个参数——属性名，属性值
    $('.div1 a').attr('href', href)  //给所有的a标签添加属性

    //移除属性
    $('a').eq(2).removeAttr('href')  //删除第三个a标签的href属性
    $('a').removeAttr('href')  //删除所有a标签的href属性


    //元素操作
    //获取元素文本
    console.log($('.div1').text())

    //获取元素的全部内容
    console.log($('.div1').html())

    //获取表单字段的值
    $('#submit').click(function (){
        var user = $('#user').val()  //获取表单中元素id属性为user的值
        var pwd = $('#pwd').val()
        //前端验证账号的长度
        if(user.length<6){
            alert('账号至少六位')
        }else {
            alert('登录成功')
        }

    })

    //在元素内部的最后面插入内容
    $('.div1').append('<b>在元素内部的最后面插入内容</b>')

    //在元素外部的后面插入内容
    $('.div1').after('<p>在元素外部的后面插入内容</p>')


})