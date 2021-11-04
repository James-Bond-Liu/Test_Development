//单行注释
/*多行注释
one
two
 */

//变量：必须有声明
var age = 20;  //声明的同时直接赋值
var name;  //先声明变量，再赋值
name = 'liufei'
//同时给多个变量赋值
var a = 10, b = 20, c = 30;

//页面弹出弹框
alert(age);
alert(name)

//输出到控制台
console.log('变量', age);
console.log(name);

//数据类型：数字类型、字符串、数组、null、undefined、Boolean
//数字类型
var a = 10;
var b = 1.33;
//字符串类型
var name = 'liufei';
//数组Array：类似于python中的列表，可以通过下标取值
var aList = Array(1, 3, 4, 'a', 'b');
aList.length;  //数组属性length，返回数组的元素数量
aList.push('python');  //往数组最后插入一个元素
aList.pop();  //删除数组最后一个元素并且返回该元素

//null类型：空类型，类似于python中的None
var c = null;

//undefined：变量已经声明，未赋值
var d;

//boolean：true false
var t = true;
var f = false;


//条件运算符
// == 只是比较内容是否相等，不管等号两边的数据类型是否相同
// === 不光比较等号两边内容是否相同，同时也要比较两边数据类型是否相同

//赋值运算符  ++  放在变量后面时，先运算后增，放在变量前面时，先增再运算。
a = 1;
a++;  //先输出a=1,然后对a增加1


//条件语句 if 语句 else if 语句 else语句
var number = 10;
if (number>100){
    alert('大于100');
}else if (number === 100){
    console.log('等于100');
} else {
    alert('小于100');
}

//switch语句
var q = 10,w=20;
switch (w-q){
    case 5:
        console.log('等于5');
        break;  //每一个条件不加break跳出的话，即使此处匹配表达式成功，代码也会一直向下继续匹配
    case 10:
        console.log('等于10');
        break;
    default:
        console.log('以上代码没有匹配成功')
}


//对象
//创建对象
var objA={
    name:'panda',  //给对象添加属性
    age:4,
}
//访问对象属性，通过对象名.键名或者对象名['键名']
objA.age;
objA['age']
//设置对象方法
var objB={
    name:'panda',  //给对象添加属性
    age:4,
    func:function (){  //对象内部设置方法的时候不需要设置函数名
        alert('*****')
    }
}
//访问对象方法等同于访问对象属性
objB.func()
objB['func']

//循环
//while循环
var i = 0;
while (i<=5){
    alert(i);
    i++
}
//for循环
var aList = Array(11,22,33);
for (var a=0;a<aList.length;a++){
    alert(aList[a]);
}
//for遍历循环
var objA ={
    name : 'liufei',
    age : 27,
    gender : 'man'
}
for (i in objA){
    console.log(i);  //name age gender
    objA[i]  //获取对象中的属性
}


    
