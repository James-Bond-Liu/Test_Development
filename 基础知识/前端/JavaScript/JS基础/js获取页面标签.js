window.onload = function func() {  //等到页面加载完后再执行这个函数，否则页面会报错找不到元素因为元素还没有加载到。
    var box2 = document.getElementById('box2');  //返回的是选中的元素
    box2.style.height='50px';  //更改元素样式style
    box2.style.width='50px';
    box2.style.background='green';

    var btn2 = document.getElementsByClassName('btn2')[0];  //返回的是选择集，一个类名为**的元素列表
    console.log(btn2);
    btn2.style.background='red';

    var list = document.getElementsByTagName('li');  //同理也是一个集合
    alert(list.length)
    for (var i=0;i<=list.length;i++){
        if (i%2==0){
            list[i].style.background='blue'
        }
    }
}