$(document).ready(function (event) {
    //function to get hello api
    function getHelloApi (){
        const code = $("#language_code").val();
        const url =  `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
        $.get(url, function (data) {
            $("#hello").text(data.hello);
        });
    }
    // click function
    $("#btn_translate").on("click", function () {
        getHelloApi();
    });

    //keypress function for enter key
   $("#language_code").on("keypress", function (action) { 
    if (action.which == 13) {
       getHelloApi();
    }
    });
});