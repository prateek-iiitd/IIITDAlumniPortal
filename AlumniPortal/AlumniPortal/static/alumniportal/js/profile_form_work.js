/**
 * Created by sauhard on 10/11/14.
 */
$(document).ready(function(){
    counter = 1;
    $(".btn-add").click(function() {
        $(this).hide();
        $("#form".concat(counter-1)).css("padding-bottom", "10px");
        $("#form".concat(counter-1)).css("background-color", "white");
        $("#form".concat(counter-1)).css("box-shadow", "none");
        $("#form".concat(counter)).css("background-color", "#F8F8F8");
        $("#form".concat(counter)).css("box-shadow", "0 0 3px 15px #F8F8F8");
        $("#form".concat(counter)).slideDown("fast");
//        $("#form".concat(counter)).delay(5000).css("background-color", "white");
//        $("#form".concat(counter)).delay(5000).css("box-shadow", "none");
        counter=counter+1;
    });
});
