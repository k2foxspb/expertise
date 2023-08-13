$(window).on('load pageshow', function () {
    $('body').removeClass("off");
    $('body').addClass("on");
});
$("a:not([href*=\\#])").click(function() {
    if (!$(this).attr('target')) {
        $('body').removeClass("on");
        $('body').addClass("off");
        let url = $(this).attr('href');
        window.setTimeout(function() {
            window.location.href = url;
        }, 400);
        return false;
    }
});