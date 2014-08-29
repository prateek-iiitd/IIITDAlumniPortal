/**
 * Created by sauhard on 30/8/14.
 */
$(document).ready(function() {
    $(".panel-heading").click(function() {
            $("#preview").fadeTo("fast", 0).delay(1);
            $v1 = $(this).parent().get(0);
//        $cont = $v1.html();
//        $("#preview .panel").html($cont);
            $("#preview").fadeTo("medium", 1);
    });
});