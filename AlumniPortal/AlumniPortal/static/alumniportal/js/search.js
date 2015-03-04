/**
 * Created by sauhard on 3/4/15.
 */
$(document).ready(function () {
    // function to request list of student details using Ajax and list all results automatically
    $.ajax({
        url: "http://192.168.49.189:8000/api/v1/basic/?format=json",
        type: "GET",
        dataType: "json",
        success: displaySearchResults,
        error: function(xhr, status, error) {
            console.log(status+' '+error);
        }
    });
    function displaySearchResults(response, status, xhr) {
        total_count = response['meta']['total_count']; // total number of search results to display
        for (var counter=0; counter<total_count; counter++) {
            var student = response['objects'][counter];
            console.log(student);
            first_name = student['first_name'];
            last_name = student['last_name'];
            // WORKPLACE HERE??? BACKEND NOOBS FFS!
            graduation_year = student['graduation_year'];

            // checking for null values
            if (!first_name) {
                first_name = '';
            }
            if (!last_name) {
                last_name = '';
            }
            if (!graduation_year) {
                graduation_year = '';
            }
            else {
                graduation_year = 'Batch '+graduation_year;
            }

            $("#search-results-right").append('<div class="row"><div class="col-lg-1"><div class="pic"></div></div><div class="col-lg-10" style="padding: 5px 0 0 25px"><p style="margin-bottom: 0">'+first_name+' '+last_name+'<br>Backend &nbsp;| &nbsp;Noobs<br> '+graduation_year+'</p></div></div><div class="divider-4r"></div>');
        }
    }
//    $("#search-results-right").append('<div class="row"><div class="col-lg-1"><div class="pic"></div></div><div class="col-lg-10" style="padding: 5px 0 0 25px"><p style="margin-bottom: 0">Sauhard Gupta<br>Adobe &nbsp;| &nbsp;Senior Scientist<br>Batch 2015</p></div></div><div class="divider-4r"></div>');
});