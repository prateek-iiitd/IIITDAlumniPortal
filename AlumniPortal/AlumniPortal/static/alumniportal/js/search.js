/**
 * Created by sauhard on 3/4/15.
 */

function displaySearchResults(response, status, xhr) {
    document.getElementById("search-results-right").innerHTML = "";
    total_count = response['meta']['total_count']; // total number of search results to display
    $('#count-search-results-right>h4:first-child>span').html(total_count);
    for (var counter = 0; counter < total_count; counter++) {
        var student = response['objects'][counter];
        console.log(student);

        // checking for null values
        id = student['id'];
        var email = student['email'];
        $("#email-overlay input").val($("#email-overlay input").val()+email+', ');
        if (!student['first_name']) {
            first_name = '';
        }
        else {
            first_name = student['first_name'];
        }
        if (!student['last_name']) {
            last_name = '';
        }
        else {
            last_name = student['last_name'];
        }

        if (!student['current_location']['city']) {
            current_location = '';
        }
        else {
            current_location = student['current_location']['city'];
        }
        if (!student['work_details'][0]) {
            organization = '';
        }
        else {
            organization = student['work_details'][0]['organisation']['name'];
        }
        if (organization != '' && current_location != '') {
            organization_and_current_location = organization +' &nbsp;| &nbsp;<span class="glyphicon glyphicon-map-marker"></span> '+current_location+'<br> ';
        }
        else {
            if (organization == '') {
                organization_and_current_location = '<span class="glyphicon glyphicon-map-marker"></span> ' + current_location+'<br> ';
            }
            else {
                if (current_location == '') {
                    organization_and_current_location = organization + '<br> ';
                }
                else {
                    organization_and_current_location = '<br> ';
                }
            }
        }

        if (!student['graduation_year']) {
            graduation_year = '<br>';
        }
        else {
            graduation_year = 'Class of ' + student['graduation_year'];
        }
        if (!student['profile_photo']) {
            profile_photo = STATIC_URL + 'alumniportal/img/user.jpg';
        }
        else {
            profile_photo = student['profile_photo'];
        }

        profile_link = '/test/profile/'+id+'/';
        console.log(student);

        $("#search-results-right").append('<a href="' + profile_link + '"><div class="row"><div class="col-lg-1"><div class="pic" style="background-image: url(' + profile_photo + ')"></div></div><div class="col-lg-10" style="padding: 5px 0 0 37px"><p style="margin-bottom: 0">' + first_name + ' ' + last_name + '<br>'+ organization_and_current_location + graduation_year + '</p></div></div></a>');
    }
}

function getAndDisplayFilters(url)
{
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: displaySearchResults,
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}

$(document).ready(function () {
    $("#email-overlay div input").val("");
    // function to request list of student details using Ajax and list all results automatically
    getAndDisplayFilters("/api/v1/filter/?format=json");

    $(document).bind('keydown', function(event) {
        if( event.which == 99 || event.which == 67 && event.ctrlKey ) {
            $("#email-overlay>div h2").html("Press <span>Ctrl+C</span> to copy!");
            $("#email-overlay>div h2 span").css("color", "#666");
            $("#email-overlay>div").delay(500).slideUp("medium");
            $("#email-overlay").delay(500).fadeOut("medium");
            $("#email-overlay-background").delay(500).fadeOut("medium");
        }
        if( event.which == 120 || event.which == 88 && event.ctrlKey ) {
            $("#email-overlay>div h2").html("Press <span>Ctrl+X</span> to cut!");
            $("#email-overlay>div h2 span").css("color", "#666");
            $("#email-overlay>div").delay(500).slideUp("medium");
            $("#email-overlay").delay(500).fadeOut("medium");
            $("#email-overlay-background").delay(500).fadeOut("medium");
        }
        if( event.which == 99 || event.which == 67 && event.metaKey ) {
            $("#email-overlay>div h2").html("Press <span>Command+C</span> to copy!");
            $("#email-overlay>div h2 span").css("color", "#666");
            $("#email-overlay>div").delay(500).slideUp("medium");
            $("#email-overlay").delay(500).fadeOut("medium");
            $("#email-overlay-background").delay(500).fadeOut("medium");
        }
        if( event.which == 120 || event.which == 88 && event.metaKey ) {
            $("#email-overlay>div h2").html("Press <span>Command+X</span> to cut!");
            $("#email-overlay>div h2 span").css("color", "#666");
            $("#email-overlay>div").delay(500).slideUp("medium");
            $("#email-overlay").delay(500).fadeOut("medium");
            $("#email-overlay-background").delay(500).fadeOut("medium");
        }
        if( event.keyCode == 27 ) {
            $("#email-overlay>div h2").html("Press <span>Esc</span> to exit!");
            $("#email-overlay>div h2 span").css("color", "#666");
            $("#email-overlay>div").delay(500).slideUp("medium");
            $("#email-overlay").delay(500).fadeOut("medium");
            $("#email-overlay-background").delay(500).fadeOut("medium");
        }
    });

    $("#btn-email-overlay").click(function() {
        $("#email-overlay").css("display", "flex");
        $("#email-overlay>div").slideDown("medium");
        $("#email-overlay-background").fadeIn("medium");
//        $("#email-overlay div input").val(email);
        $("#email-overlay div input").focus().select();
    });

    $("#email-overlay-background").click(function() {
        $("#email-overlay>div").slideUp("medium");
        $("#email-overlay").fadeOut("medium");
        $("#email-overlay-background").fadeOut("medium");
    });
//    $("#search-results-right").append('<div class="row"><div class="col-lg-1"><div class="pic"></div></div><div class="col-lg-10" style="padding: 5px 0 0 25px"><p style="margin-bottom: 0">Sauhard Gupta<br>Adobe &nbsp;| &nbsp;Senior Scientist<br>Batch 2015</p></div></div><div class="divider-4r"></div>');
});

function append_filter_text(filter, id) {
    if (document.getElementById(id).value != "")
        return "&" + filter + "=" + document.getElementById(id).value;
    return "";
}

function append_filter_select(filter, id) {
    if (document.getElementById(id).value != "-1")
        return "&" + filter + "=" + document.getElementById(id).value;
    return "";
}

function append_filter_checkbox(filter, id) {
    if (document.getElementById(id).checked)
        return "&" + filter + "=" + document.getElementById(id).checked;
    return "";
}

function filterList() {

    $("#email-overlay input").val('');

    url = "/api/v1/filter/?format=json"
    url += append_filter_text("first_name__istartswith", "id_name");
    url += append_filter_select("gender__iexact", "id_gender");
    url += append_filter_text("graduation_year__lte", "id_batch");
    url += append_filter_text("graduation_year__gte", "id_batch");
    url += append_filter_text("current_location__city__icontains", "id_curr_city");
    url += append_filter_text("current_location__country__name__iexact", "id_curr_country");
    url += append_filter_text("educations__school__name__icontains", "id_university_name");
    url += append_filter_text("educations__school__location__city__icontains", "id_degree_city");
    url += append_filter_text("educations__school__location__country__name__iexact", "id_degree_country");
    url += append_filter_select("educations__degree_type__name__iexact", "id_degree_type");
    url += append_filter_text("work_details__organisation__name__icontains", "id_company_name");
    url += append_filter_text("work_details__organisation__location__city__icontains", "id_profession_city");
    url += append_filter_text("work_details__organisation__location__country__name__iexact", "id_profession_country");
    url += append_filter_select("work_details__work_type__name__iexact", "id_profession_type");
    url += append_filter_checkbox("educations__is_current", "id_degree_is_current");
    url += append_filter_checkbox("work_type__is_current", "id_degree_is_current");
    getAndDisplayFilters(url);
    window.scrollTo(0,0);

}