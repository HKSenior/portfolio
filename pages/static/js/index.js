let brandClicked = false;
let scrollPos = 0;
let scrollDir = "";

particlesJS.load('particles-js', 'static/particles.json', function () {
    console.log('particles.js config loaded');
});


(function ($) {
    $(document).ready(function () {
        $(".navbar").hide();
        $(function () {
            $(window).scroll(function () {
                if (scrollDir === 'DOWN' && brandClicked === false) {
                    $('.navbar').removeClass('d-none');
                    if ($(this).scrollTop() > 500) {
                        $('.navbar').fadeIn();
                    } else {
                        $('.navbar').fadeOut();
                    }
                } else if (scrollDir === 'UP' && brandClicked === false) {
                    if ($(this).scrollTop() < 500) {
                        $('.navbar').fadeOut();
                    }
                }
            });
        });
    });
}(jQuery));


window.addEventListener('scroll', function(){
    if ((document.body.getBoundingClientRect()).top > scrollPos)
        scrollDir = 'UP'
    else
        scrollDir = 'DOWN'
    scrollPos = (document.body.getBoundingClientRect()).top;
});
document.getElementById('nav-brand').addEventListener('click', () => {
    brandClicked = true;
    $('.navbar').fadeOut();
    $('html, body').animate({
        scrollTop: 0
    }, 100);
    setTimeout(() => {
        brandClicked = false;
    }, 100);
});
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
        scrollTop: ($('#contact').offset().top)
    }, 100);
});


setTimeout(function() {
    $('#message').fadeOut('slow')
}, 3000);
