particlesJS.load('particles-js', 'static/particles.json', function () {
    console.log('particles.js config loaded');
});

(function ($) {
    $(document).ready(function () {
        $(".navbar").hide();
        $(function () {
            $(window).scroll(function () {
                $('.navbar').removeClass('d-none');
                if ($(this).scrollTop() > 500) {
                    $('.navbar').fadeIn();
                } else {
                    $('.navbar').fadeOut();
                }
            });
        });
    });
}(jQuery));

document.getElementById('nav-skills').addEventListener('click', () => {
    $('html, body').animate({
        scrollTop: ($('#skills').offset().top)
    }, 100);
});

document.getElementById('nav-projects').addEventListener('click', () => {
    $('html, body').animate({
        scrollTop: ($('#projects').offset().top)
    }, 100);
});
document.getElementById('nav-resume').addEventListener('click', () => {
    $('html, body').animate({
        scrollTop: ($('#resume').offset().top)
    }, 100);
});
document.getElementById('nav-contactme').addEventListener('click', () => {
    $('html, body').animate({
        scrollTop: ($('#resume').offset().top)
    }, 100);
});
