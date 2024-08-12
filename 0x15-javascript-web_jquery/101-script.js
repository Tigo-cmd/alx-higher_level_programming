$(document).ready(() => {
    $("#add_item").on("click", () => {
        $(".my_list").append("<li>Item</li>");
    });

    $("#remove_item").on("click", function () {
        $(".my_list li:Last-child").remove();
    });
 
    $("#clear_list").on("click", () => {
        $(".my_list").empty();
    });
});