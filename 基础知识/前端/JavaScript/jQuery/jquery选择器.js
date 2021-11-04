//创建函数，让页面加载完成后再执行js、jQuery脚本。等同于window.onload=function (){}
$(function (){

    //jquery 选择器
    $('#box1').css({background:'red',width:'500px'})  //css修改元素样式，注意不同key之间用“，”分隔，value值用‘’引号引起来

    $('li').css({background: 'blue', height:'20px'})  //通过标签选择

    $('p[name=user]').css({background:'green'})  //通过标签属性选择

    //选择<li id="li3">的所有同辈元素,不包括自己本身
    $('#li3').siblings().css({background:'#bd2997'})

    //选择<li id="li1">的父元素<ul>的父元素<div>的之前紧挨的同辈元素<p>
    var li =$('#li1').css({background:'red'});
    var ul=li.parent();
    var div=ul.parent();
    var p=div.prev().css({textAlign:'center'});
    //使用链式调用,等同于上面一步一步调用
    $('#li1').css({background:'red'}).parent().parent().prev().css({textAlign:'center'});

    //选择div标签内，id=li4的标签
    $('div').find('#li4').css({float:'right'})

    //选择过滤，选择class属性为btn2的div标签
    $('div').filter('.btn2').css({textAlign: 'center'})
    // 选择过滤，通过索引选择第三个li标签
    $('li').eq(2).css({background: 'black'})

    //获取元素的索引值
    console.log($('#li3').index())  //输出2
})

