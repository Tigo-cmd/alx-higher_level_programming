// $('#red_header').on("click", function() {
//     $('header').css('color', '#FF0000');
// });

function toRedColor() {
    $("header").css(
        'color',
        '#FF0000'
    );
}

$("#red_header").on("click", toRedColor);