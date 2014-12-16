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
      $("#dropdownMenu1:first-child").text($(this).text());
      $("#dropdownMenu1:first-child").val($(this).text());
    });
   });
});

function yearSelected(element) {
    $("#btech_col0").html("");
    $("#btech_col1").html("");
    $("#btech_col2").html("");
    $("#mtech_col0").html("");
    $("#mtech_col1").html("");
    $("#mtech_col2").html("");
    $("#dual_col0").html("");
    $("#dual_col1").html("");
    $("#dual_col2").html("");
    $("#phd_col0").html("");
    $("#phd_col1").html("");
    $("#phd_col2").html("");
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
        var btech_index = 0;
        var mtech_index = 0;
        var dual_index = 0;
        var phd_index = 0;

        for (i = 0, len = students.length; i < len; i++) {
            var template = temp;
            template = template.replace("identifier_name", students[i].name);
            template = template.replace("identifier_info", students[i].degree + " - " + students[i].graduation_year.toString());
            template = template.replace("identifier_iiitd_email", students[i].iiitd_email);

            if(students[i].degree == 'B.Tech.')
            {
                $("#btech_col" + (btech_index % 3).toString()).append(template);
                btech_index += 1;
            }
            else if(students[i].degree == 'M.Tech.')
            {
                $("#mtech_col" + (mtech_index  % 3).toString()).append(template);
                mtech_index += 1;
            }
            else if(students[i].degree == 'Dual')
            {
                $("#dual_col" + (dual_index % 3).toString()).append(template);
                dual_index += 1;
            }
            if(students[i].degree == 'Ph.D.')
            {
                $("#phd_col" + (phd_index % 3).toString()).append(template);
                phd_index += 1;
            }

        }
//
//        console.log("btechs : " + btech_index.toString())
//        console.log("mtechs : " + mtech_index.toString())
//        console.log("phd : " + phd_index.toString())
//        console.log("dual : " + dual_index.toString())
        if(btech_index == 0)
            $("#no_betch").css("display", "block");
        if(mtech_index == 0)
            $("#no_metch").css("display", "block");
        if(phd_index == 0)
            $("#no_phd").css("display", "block");
        if(dual_index == 0)
            $("#no_dual").css("display", "block");

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