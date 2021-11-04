$(function (){

    //点击登录按钮发起Ajax请求
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
                console.log(data);
                alert('登录成功')
            },
            error: function (){     //当Ajax请求失败之后，会自动触发这个回调函数
                alert('登录失败')
            }
        });
    })

    // 将id=‘pro’选择框的数据从后端得到，然后添加到前端HTML中
    $.ajax({
        url:'pro_list',
        method:'get',
        dataType:'json',
    }).done(function (data){
        var pro = $('#pro');
        var res = data.data;
        //遍历数据
        for (i in res){
            var option = '<option varlue='+res[i].id+'>'+res[i].title+'</option>';
            pro.append(option);
        }
        })

    // change事件：检测元素值是否发生变化
    var pro = $('#pro');
    pro.change(function (){
        // 往接口列表发送ajax请求
        // 参数pro_id
        var pro_id = pro.val();
        $.ajax({
            url:'/interface',
            data: {'pro_id': pro_id},
            type: 'post',
            dataType: 'json'
        }).done(function (data){
            // 定位到接口的下拉框
            var inter = $('#interface');
            if (data.code==='1'){
                inter.empty();
                var res = data.data;
                // 遍历返回的数据，然后将数据添加到id=interface的下拉框中
                for(var i = 0; i<res.length; i+11){  // 第二种for循环的方式
                    var option = '<option value="">'+res[i].name+'</option>';
                    inter.append(option);
                }

            }
        })

    })
})