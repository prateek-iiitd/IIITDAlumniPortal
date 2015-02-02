/**
 * Created by sauhard on 10/11/14.
 */
$(document).ready(function(){
    counter = 1;
    $(".btn-add").click(function() {
        $("#form".concat(counter)).slideDown("fast");
        counter=counter+1;
    });
});
