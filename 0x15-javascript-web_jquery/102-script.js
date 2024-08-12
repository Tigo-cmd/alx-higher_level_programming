$(document).ready(function () {
    $("#btn_translate").on("click", () => {
        const code = $("#language_code").val();
        const url = `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
        $.get(url, function (data) {
                $("#hello").text( () => {
                    return data.hello;
                });
            });
    });
});