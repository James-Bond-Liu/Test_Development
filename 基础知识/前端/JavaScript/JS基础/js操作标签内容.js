window.onload=function (){
    var box2=document.getElementById('box2');
    console.log(box2.innerHTML);  //读取页面元素内容

    var btn1=document.getElementsByClassName('btn1')[0];
    console.log(btn1.innerHTML);  //读取页面元素的全部内容，即使标签下仍然含有标签也依然能获取到
    console.log(btn1.innerText);  //只获取页面元素下的文本内容

    box2.innerHTML='python永远的神';  //修改页面元素的内容

    var input=document.getElementsByTagName('input')[0];
    console.log(input.type);  //获取元素属性
    input.type='password';  //修改元素属性

}
//定义一个函数，用于html元素事件绑定
function tankuang() {
    alert('中国');
    alert('China')

}