$(function (){
    //弹框
    $('#add').click(function (){
        //点击主题内容中的➕，通过增加一个show属性，然后显示弹框
        // $('.alter_add').addClass('show');
        $('.back').slideDown();
    });
    $('.alter_quit').click(function (){
        //点击弹框中的取消X按钮，通过删除show属性，退出弹框
        // $('.alter_add').removeClass('show');
        $('.back').slideUp();
    })
    $('.pro_tj').click(function (){
        //点击弹框中的提交，退出弹框
        $('.back').slideUp();
    })


    //侧边栏
    $('.left_menu_list h3').click(function (){
        //重复切换，当第一次点击元素如果没有show属性，则增加show属性，然后再点击一次则删除show属性。依次往复
        // $(this).next().toggleClass('show').parent().siblings().children('ul').removeClass('show')
        //利用jQuery动画实现
        $(this).next().toggle().parent().siblings().children('ul').hide()
    })

})