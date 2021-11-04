$(function (){
    $('.menu li').click(function (){
        $(this).addClass('cur').siblings().removeClass('cur');
        $('.content div').eq($(this).index()).addClass('active').siblings().removeClass('active')
    })

    //添加数据
    var data="<tr>\n" +
        "                    <td><input type=\"radio\"></td>\n" +
        "                    <td><input type=\"text\"></td>\n" +
        "                    <td><input type=\"text\"></td>\n" +
        "                </tr>"
    //当点击添加数据按钮后，增加一行
    $('.add_data').click(function (){
        //获取当前table的最后一行tr的内容再添加
        var tr = '<tr>'+$(this).siblings('table').find('tr').eq(-1).html()+'</tr>'
        $(this).siblings('table').append(tr)
    })

    //点击删除数据按钮，然后匹配最后一行tr，删除最后一行
    // $('.del_data').click(function (){
    //     $(this).siblings('table').find('tr').eq(-1).remove()
    // })

    //删除被选中的行
    $('.del_data').click(function (){
        var check = $(':checked')  //获取被选中的input元素
        var table = $(this).siblings('table')
        // 先判断table标签下的tr标签数目是否大于2，防止将第一行的表格删除掉
        // 再判断被选中的radio是否大于0，大于0删除被选中的，否则默认删除最后一行
        if(table.find('tr').length>2) {
            if(check.length>0){
                check.parent().parent().remove();  //:checked选择器，匹配所有被选择的input元素
            }else {
                table.find('tr').eq(-1).remove();
            }
        }
    })
})