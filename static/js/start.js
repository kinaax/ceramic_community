$(document).ready(function () {
    function handleMouseWheel(event) {
        var delta = event.deltaY || event.wheelDelta; 
        // 滚轮上滚的时候触发
        if (delta < 0) {
            $('.title h2').css({ "left": "50%", "width": "560px", "fontSize": "32px" })
            $('.shellstyle').css({
                "display": "block",
            })
            $('.shell').css({
                "background-color": "#fffef8",
                "color": "#2F318B",
            })
            $('.box').css({ "background": "#2F318B" })
            $('.one').css({
                "width": "11px",
                "height": "11px",
                "background": "#fffef8",
                "border": "7px solid #2F318B",
            })
            $('.two').css({
                "width": "18px",
                "height": "18px",
                "background": "#2F318B",
            })
            $('.one .line').css({ "opacity": "1" })
            $('.two .line').css({ "opacity": "0" })
            $('.two span').css({ "opacity": "0" })
            $('.one span').css({ "opacity": "1" })
            $('.circle').css({
                "left": "145px",
                "background-size": "cover",
            })
            $('.main h2').css({
                "width": "800px",
                "height": "300px",
                "top": "150px",
                "left": "0px",
                "fontSize": "200px",
                "color": "#2F318B",
            })
            $('.main h2').text('人间瓷话')
            $('.content').css({ "opacity": "0", "top": "260px" })
        }
        // 滚轮下滚的时候触发
        else if (delta > 0) {
            $('.title h2').css({ "left": "90px", "width": "100px", "fontSize": "24px" })
            $('.shellstyle').css({
                "display": "none",
            })
            $('.shell').css({
                "background-color": "#2F318B",
                "color": "#fffef8",
            })
            $('.box').css({ "background": "#fffef8" })
            $('.two').css({
                "width": "11px",
                "height": "11px",
                "background": "#2F318B",
                "border": "7px solid #fffef8",
            })
            $('.one').css({
                "width": "18px",
                "height": "18px",
                "background": "#fffef8",
            })
            $('.two .line').css({ "opacity": "1" })
            $('.two span').css({ "opacity": "1" })
            $('.one span').css({ "opacity": "0" })
            $('.circle').css({
                "left": "-150px",
                "background-size": "700px",
            })
            $('.main h2').css({
                "left": "-300px",
                "fontSize": "150px",
                "color": "#fffef8",
            })
            $('.main h2').text('欢迎参观')
            $('.content').css({ "opacity": "1", "top": "160px" })
        }
    }

    // 添加滚轮事件监听器
    if (window.addEventListener) {
        window.addEventListener('wheel', handleMouseWheel);
    } else if (window.attachEvent) { // 兼容IE
        window.attachEvent('onmousewheel', handleMouseWheel);
    }
});