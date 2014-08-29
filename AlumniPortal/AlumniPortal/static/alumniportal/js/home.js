/**
 * Created by sauhard on 29/8/14.
 */
$(document).ready(function() {
    $(".panel-heading").click(function() {
        $var1 = $(this).parent().get(0);
        if($var1.children[1].style.display=="" || $var1.children[1].style.display=="none") {
            $(".panel-body").slideUp("fast");
            $($var1.children[1]).slideDown("fast");
        }
    });
});