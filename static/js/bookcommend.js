// JavaScript source code
$(function () {
    $("#readlink").hover(function () {
        $(".way").css("display", "block");
    }, function () {
        $(".way").css("display", "none");
    })
    // 切换大图片
    $('.b_l_bottom li').click(function () {
        $(this).addClass('on').siblings().removeClass("on");
        $(".b_l_top > li").hide().eq($('.b_l_bottom li').index(this)).show();
    });
    // 选择标签保持变色
    $('.opt .choice').mouseover(function () {
        $(this).addClass('on').siblings().removeClass("on");
    });
    // 悬停变换介绍内容
    $('.content_intro_list li a').mouseover(function () {
        $(this).addClass('on').parent().siblings().find("a").removeClass("on");
        $(".content_intro > div").hide().eq($('.content_intro_list li a').index(this)).show();
    });
    $('.bar_list li').click(function () {
        var index = $(this).index();
        $(this).find("a").addClass('on').parent().siblings().find("a").removeClass("on");
        $(this).parent().parent(".bar").find(".inside li").stop(true, true).not(':eq(' + index + ')').hide();
        $(this).parent().parent(".bar").find(".inside li").eq(index).show();
    });
})