/**
 * Created by sauhard on 30/8/14.
 */
/**
 * Created by sauhard on 29/8/14.
 */
$(document).ready(function () {
    console.log("JS connecting");
    $("#openfeedback").click(function() {
        console.log("Clicking");
        $("#black").css("z-index", 999).fadeTo("medium", 0.7);
        $("#feedback").css("z-index", 1000).slideDown("fast");
//        $("#feedback").css("z-index", 1000).fadeTo("medium", 1);
    });
    $("#feedback #close").click(function () {
        $("#black").fadeTo("medium", 0).css("z-index", -1);
        $("#feedback").slideUp("fast").css("z-index", -1);
    });
    $("#black").click(function () {
        $("#black").fadeTo("medium", 0).css("z-index", -1);
        $("#feedback").slideUp("fast").css("z-index", -1);
    });
    $(document).keydown(function(e) {
    // ESCAPE key pressed
        if (e.keyCode == 27) {
            $("#black").fadeTo("medium", 0).css("z-index", -1);
            $("#feedback").slideUp("medium").css("z-index", -1);
        }
    });
});