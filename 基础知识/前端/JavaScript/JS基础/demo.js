var aList={
    name :'liufei',
    age : 10,
    gender : 'man',
    func:function (){
        alert('*****')
    }
}
aList.func()

for (i in aList){
    console.log(i)
    console.log(aList[i])
}