/**
 * Created by sauhard on 3/4/15.
 */

function displaySearchResults(response, status, xhr) {
    document.getElementById("search-results-right").innerHTML = "";
    total_count = response['meta']['total_count']; // total number of search results to display
    $('#count-search-results-right>h4:first-child>span').html(total_count);
    for (var counter = 0; counter < total_count; counter++) {
        var student = response['objects'][counter];
//        console.log(student);

        // checking for null values
        id = student['id'];
        email = student['email'];
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
        // WORKPLACE HERE??? BACKEND NOOBS FFS!
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

        profile_link = '/test/profile/';

        $("#search-results-right").append('<a href="' + profile_link + '"><div class="row"><div class="col-lg-1"><div class="pic" style="background-image: url(' + profile_photo + ')"></div></div><div class="col-lg-10" style="padding: 5px 0 0 37px"><p style="margin-bottom: 0">' + first_name + ' ' + last_name + '<br>Backend &nbsp;| &nbsp;Noobs<br> ' + graduation_year + '</p></div></div></a>');
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
    getAndDisplayFilters("/api/v1/basic/?format=json");

    $(document).bind('keydown', function(event) {
        if( event.which == 99 || event.which == 67 && event.ctrlKey ) {
            $("#email-overlay>div").slideUp("medium");
            $("#email-overlay").fadeOut("medium");
        }
        if( event.which == 120 || event.which == 88 && event.ctrlKey ) {
            $("#email-overlay>div").slideUp("medium");
            $("#email-overlay").fadeOut("medium");
        }
        if( event.which == 99 || event.which == 67 && event.metaKey ) {
            $("#email-overlay>div").slideUp("medium");
            $("#email-overlay").fadeOut("medium");
        }
        if( event.which == 120 || event.which == 88 && event.metaKey ) {
            $("#email-overlay>div").slideUp("medium");
            $("#email-overlay").fadeOut("medium");
        }
        if( event.keyCode == 27 ) {
            $("#email-overlay>div").slideUp("medium");
            $("#email-overlay").fadeOut("medium");
        }
    });

    $("#btn-email-overlay").click(function() {
        $("#email-overlay").css("display", "flex");
        $("#email-overlay>div").slideDown("medium");
        $("#email-overlay div input").focus().select();
    });

    $("#email-overlay").click(function() {
        $("#email-overlay>div").slideUp("medium");
        $("#email-overlay").fadeOut("medium");
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

    url = "/api/v1/filter/?format=json"
    url += append_filter_text("first_name__icontains", "id_name");
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

}