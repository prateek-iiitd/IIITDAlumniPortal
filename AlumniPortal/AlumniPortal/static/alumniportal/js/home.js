/**
 * Created by sauhard on 29/8/14.
 */
$(document).ready(function () {
    $(".panel-heading").click(function () {
        $var1 = $(this).parent().get(0);
        if ($var1.children[1].style.display == "" || $var1.children[1].style.display == "none") {
            $(".panel-body").slideUp("fast");
            $($var1.children[1]).slideDown("fast");
        }
    });
    $("#openfeedback").click(function() {
        $("#black").css("z-index", 999).fadeTo("medium", 0.7);
        $("#feedback").css("z-index", 1000).slideDown("medium");
//        $("#feedback").css("z-index", 1000).fadeTo("medium", 1);
    });
    $("#black").click(function () {
        $("#black").fadeTo("medium", 0).css("z-index", -1);
        $("#feedback").slideUp("medium").css("z-index", -1);
    });
    $(document).keydown(function(e) {
    // ESCAPE key pressed
        if (e.keyCode == 27) {
            $("#black").fadeTo("medium", 0).css("z-index", -1);
            $("#feedback").slideUp("medium").css("z-index", -1);
        }
    });
});