/**
 * Created by sauhard on 3/5/15.
 */
$(document).ready(function () {
    $.ajax({
        url: "/test/test_json_data/",
        type: "GET",
        dataType: "json",
        success: populateProfile,
        error: function (xhr, status, error) {
            alert(status + ' ' + error);
        }
    });
    function populateProfile(response, status, xhr) {
        student = response['objects'][0];
        if (student['profile_photo']) {
            $('.pic').css('background-image', 'url("'+student['profile_photo']+'")')
        }
        if (!student['graduation_year']) {
            graduation_year = '<br>';
        }
        else {
            graduation_year = 'Class of '+student['graduation_year'];
        }
        if (!student['work_details']) {
            work_details = '<br>';
        }
        else {
            work_details = student['work_details'];
            for (work_detail in student['work_details']) {
                if (work_detail['is_current']) {
                    if (!work_detail['organisation']['name']) {
                        organisation = '';
                    }
                    else {
                        organisation = work_detail['organisation']['name'];
                    }
                    if (!work_detail['title']) {
                        designation = '<br>';
                    }
                    else {
                        designation = ' &nbsp;| &nbsp;'+work_detail['title']+'<br>';
                    }
                }
                else {
                    organisation = '';
                    designation = '<br>';
                }
            }
        }
        $("#banner>div.image>p").html('<span>'+student['first_name']+' '+student['last_name']+'</span><br>'
                +organisation+designation
                +graduation_year);

        if (student['linkedin_profile']=='') {
            linkedin_profile='';
        }
        else {
            linkedin_profile = '<a href="'+student['linkedin_profile']+'"><div class="social-btns-li"></div></a>';
        }
        if (student['facebook_profile']=='') {
            facebook_profile='';
        }
        else {
            facebook_profile = '<a href="'+student['facebook_profile']+'"><div class="social-btns-fb"></div></a>';
        }
        if (student['google_profile']=='') {
            google_profile='';
        }
        else {
            google_profile = '<a href="'+student['google_profile']+'"><div class="social-btns-gp"></div></a>';
        }
        if (student['twitter_profile']=='') {
            twitter_profile='';
        }
        else {
            twitter_profile = '<a href="'+student['twitter_profile']+'"><div class="social-btns-tw"></div></a>';
        }
        $("div.social-btns").html(linkedin_profile+facebook_profile+google_profile+twitter_profile);
    }
});