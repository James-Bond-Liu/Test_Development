
// 当发起的Ajax请求地址并不是后端服务器地址，而是一个其他服务器时，就叫做Ajax跨域请求
$(function (){
    $.ajax({
        url:'https://www.baidu.com',
        method:'post',
        data:{'user':'**', 'pwd':'**'},
        dataType:'jsonp',  //jsonp的数据格式用来接收跨域请求返回的数据
    }).done(function (data){
        alert(data.code);
    })
})