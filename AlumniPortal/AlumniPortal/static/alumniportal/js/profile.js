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

        // setting social links
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

        // setting work and education
        if (!student['work_details']) {
            work_details = '<br>';
        }
        else {
            work_details = student['work_details'];
            for (i=0; i<student['work_details'].length; i++) {
                if (work_details[i]['is_current']) {
                    if (!work_details[i]['organisation']['name']) {
                        organisation = '';
                    }
                    else {
                        organisation = work_details[i]['organisation']['name'];
                    }
                    if (!work_details[i]['title']) {
                        designation = '<br>';
                    }
                    else {
                        designation = ' &nbsp;| &nbsp;'+work_details[i]['title']+'<br>';
                    }
                    console.log(work_details[i]);
                    break;
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
        for (i=0; i<student['work_details'].length; i++) {
            if (!work_details[i]['organisation']['name']) {
                organisation = '';
            }
            else {
                organisation = work_details[i]['organisation']['name'];
            }
            if (!work_details[i]['title']) {
                designation = '<br>';
            }
            else {
                designation = work_details[i]['title'];
            }
            if (!work_details[i]['start_date'] && !work_details[i]['end_date']) {
                start_date = '';
                end_date = '';
            }
            else {
                if (!work_details[i]['start_date']) {
                    start_date = ', ';
                    end_date = ' Till '+work_details[i]['end_date'];
                }
                else {
                    if (!work_details[i]['end_date']) {
                        start_date = ', Started ' + work_details[i]['start_date'];
                        end_date = '';
                    }
                    else {
                        start_date = ', ' + work_details[i]['start_date'];
                        end_date = ' - ' + work_details[i]['end_date'];
                    }
                }
            }
            $('div.work-and-education>div.row:first-child').append('\
                <div style="margin-left: 15px;padding-left: 10px;border-left:1px #666 solid;" class="h4-big">\
                    <h4>'+organisation+'</h4>\
                    <span>'+designation+start_date+end_date+'</span>\
                </div>\
                ');
        }
    }
});