
//ajax请求步骤，获取账号、密码；相关数据加密处理；发送ajax请求；

// 发送Ajax请求的注意点：
    // 第一点：熟悉jQuery选择器，去页面上获取请求的数据
    // 第二点：发送Ajax请求
    // 第三点：将后端返回的数据加载到页面，通过jQuery操作页面元素、属性实现


$(function (){
    //方式一
    $('#dl').click(function (){
        //读取账号密码
        var user = $('#username').val();
        var pwd = $('#password').val();
        //发送Ajax请求
        $.ajax({
            url: '/login',
            dataType: 'json',
            method: 'POST',
            data: {'user': user, 'pwd': pwd},
            success: function (data){   // 当Ajax请求成功之后，返回的数据将会作为参数传入这个方法中，返回的数据传入function（data)。
                if(data.code==='1') {
                    alert(data.msg);
                }else {
                    $(this).next().append(data.msg)
                }
            },
            error: function (){     //当Ajax请求失败之后，会自动触发这个回调函数
                alert('登录失败')
            }
        });
    })


    //方式二
    $('#dl').click(function (){
        //读取账号密码
        var user = $('#username').val();
        var pwd = $('#password').val();
        //发送Ajax请求
        $.ajax({
            url: '/login',
            dataType: 'json',
            method: 'POST',
            data: {'user': user, 'pwd': pwd}
        }).done(function (data) {            //ajax请求成功后出发done部分的回调函数
            if(data.code==='1'){
                alert(data.msg);
            }else {
                $(this).next().append(data.msg);
            }
        }).fail(function (){            //ajax请求失败后触发fail部分的回调函数
            alert('请求失败');
        })

    })
    
})
