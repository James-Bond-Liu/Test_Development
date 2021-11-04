$(function (){
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

    //change事件

})