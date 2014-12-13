/**
 * Created by sauhard on 30/8/14.
 */

$( document ).ready(function() {
//  $(".dropdown-menu li a").click(function(){
//
//  $(this).parents(".dropdown").find('.selection').text($(this).text());
//  $(this).parents(".dropdown").find('.selection').val($(this).text());
//
//});
   $(".filter-all").mouseenter(function() {
       $(this).parent().parent().children(".filter-individual").children().addClass("highlight");
       $(this).parent().parent().children(".filter-individual").children().css("width", "150px");
       $(this).parent().parent().children(".filter-individual").children().css("padding-left", "70px");
   });
   $(".filter-all").mouseleave(function() {
       $(this).parent().parent().children(".filter-individual").children().removeClass("highlight");
       $(this).parent().parent().children(".filter-individual").children().css("width", "110px");
       $(this).parent().parent().children(".filter-individual").children().css("padding-left", "52px");
       $(this).parent().parent().children(".filter-individual").children(".filter-individual-1").css("padding-left", "55px");
       $(this).parent().parent().children(".filter-individual").children(".filter-individual-2").css("padding-left", "48px");
   });
   $(".filter-individual>span").mouseenter(function() {
       $(this).addClass("highlight");
       $(this).css("width", "150px");
       $(this).css("padding-left", "70px");
       $(this).parent().parent().children(".col-lg-2").children().addClass("highlight");
   });
   $(".filter-individual>span").mouseleave(function() {
       $(this).removeClass("highlight");
       $(this).css("width", "110px");
       $(this).css("padding-left", "52px");
       $(this).parent().children(".filter-individual-1").css("padding-left", "55px");
       $(this).parent().children(".filter-individual-2").css("padding-left", "48px");
       $(this).parent().parent().children(".col-lg-2").children().removeClass("highlight");
   });
   $(function(){
    $(".dropdown-menu").on('click', 'li a', function(){
      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text());
    });
   });
});

function yearSelected(element) {
    $("#col0").html("");
    $("#col1").html("");
    $("#col2").html("");
    $("#preview").hide();
    var year = element;

    $.ajax({
        type: "GET",
        url: "/directory/batch/",
        data: { year: year },
        dataType: "json"
    })
        .done(function (msg) {
            var students = msg.students;
            var temp = msg.html;

            for (i = 0, len = students.length; i < len; i++) {
                var template = temp;
                template = template.replace("identifier_name", students[i].name);
                template = template.replace("identifier_info", students[i].degree + " - " + students[i].graduation_year.toString());
                template = template.replace("identifier_iiitd_email", students[i].iiitd_email);
                var index = i % 3;
                $("#col" + index.toString()).append(template);
            }

            $(".panel-heading").click(function () {
                $("#preview").fadeTo("fast", 0).delay(1);
                $v1 = $(this).parent().get(0);
//                var div = document.createElement('div');
//                div.innerHTML
                $("#preview .panel").html($v1.cloneNode(true));
                $("#preview").fadeTo("medium", 1);
            });
            $("#preview .panel-heading").click(function () {
                $("#preview").stop(true);
            });
        });
}