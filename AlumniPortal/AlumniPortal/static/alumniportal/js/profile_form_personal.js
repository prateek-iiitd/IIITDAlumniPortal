/**
 * Created by ankur on 3/6/15.
 */
function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

//validate functions
function personal_email_validate() {
    console.log("rh");
    var email_add = $('input#id_personal_email').val();
    if (email_add != "") {
        if (!isEmail(email_add)) {
            console.log("Email not valid.");
            $('#id_personal_email_errors').css('display', 'block');
            $('input#id_personal_email').css('border', '1px solid #A00');
        }

    }
}

function facebook_profile_validate() {
    var fb_url = $('input#id_facebook_profile').val();
    if (fb_url != "") {
        if (fb_url.toLowerCase().indexOf('facebook.com') == -1) {
            $('#id_facebook_profile_errors').css('display', 'block');
            $('input#id_facebook_profile').css('border', '1px solid #A00');
        }

    }
}

function google_profile_validate() {
    var google_url = $('input#id_google_profile').val();
    if (google_url != "") {
        if (google_url.toLowerCase().indexOf('plus.google.com') == -1) {
            $('#id_google_profile_errors').css('display', 'block');
            $('input#id_google_profile').css('border', '1px solid #A00');
        }

    }
}

function twitter_profile_validate() {
    var twitter_url = $('input#id_twitter_profile').val();
    if (twitter_url != "") {
        if (twitter_url.toLowerCase().indexOf('twitter.com') == -1) {
            $('#id_twitter_profile_errors').css('display', 'block');
            $('input#id_twitter_profile').css('border', '1px solid #A00');
        }

    }
}

function linkedin_profile_validate() {
    var lin_url = $('input#id_linkedin_profile').val();
    if (lin_url != "") {
        if (lin_url.toLowerCase().indexOf('linkedin.com') == -1) {
            $('#id_linkedin_profile_errors').css('display', 'block');
            $('input#id_linkedin_profile').css('border', '1px solid #A00');
        }

    }
}

function homepage_validate() {
    var hp = $('input#id_homepage').val();
    if (hp != "") {
        if (hp.toLowerCase().indexOf('.') == -1) {
            $('#id_homepage_errors').css('display', 'block');
            $('input#id_homepage').css('border', '1px solid #A00');
        }

    }
}

//variables
var country_selectize;
var citySelectize;
var country_data;
var city_data;
var user_data = {};
var full_user_data = {};

function set_user_data(data)
{
    full_user_data  = data;
    user_data = full_user_data['objects'][0];

}

function set_city_data(data)
{
    city_data = data;
}

function set_country_data(data)
{
    country_data = data;
}

//Function to populate the HTML form with user data received from the API
function populateUserData() {
    console.log(user_data);
    first_name = user_data['first_name'];
    last_name = user_data['last_name'];
    display_name = first_name + " " + last_name;

    $('input#id_name').val(display_name);
    $('input#id_email').val(user_data['email']);
    $('input#id_personal_email').val(user_data['personal_email']);

    $('select#id_gender').val(user_data['gender']);
    $('select#id_marital_status').val(user_data['marital_status']);

    if (user_data['current_location']['city']) {
        citySelectize[0].selectize.setValue(user_data['current_location']['city']);
    }

    if (user_data['current_location']['country']) {
        country_selectize[0].selectize.setValue(user_data['current_location']['country']['resource_uri']);
    }

    if (user_data['profile_photo']) {
        image_content_type = user_data['profile_photo']['content-type'];
        image_data = user_data['profile_photo']['file'];
        image_b64_url = 'data:' + image_content_type + ';base64,' + image_data;
        $('#id_profile_photo').css("background-image", "url('" + image_b64_url.replace(/(\r\n|\n|\r)/gm, "") + "')");
    }

    $('input#id_linkedin_profile').val(user_data['linkedin_profile']);
    $('input#id_facebook_profile').val(user_data['facebook_profile']);
    $('input#id_twitter_profile').val(user_data['twitter_profile']);
    $('input#id_google_profile').val(user_data['google_profile']);
    $('input#id_homepage').val(user_data['homepage']);

}

function populateCountrySelectList() {
    for (i = 0; i < country_data.length; i++) {
        country_name = country_data[i]['name'];
        country_uri = country_data[i]['resource_uri'];
        $('#id_country').append($('<option>', {
            value: country_uri,
            text: country_name
        }));
    }

    country_selectize = $('#id_country').selectize({
        create: false,
        sortField: 'text'
    });
}

function populateCitySelectList() {
    for (i = 0; i < city_data.length; i++) {
        city_name = city_data[i]['city'];
        $('#id_city').append($('<option>', {
            value: city_name,
            text: city_name
        }));
    }
    citySelectize = $('#id_city').selectize({
        create: true,
        persist: false,
        sortField: 'text'
    });

}

var handleFileSelect = function (evt) {
    var files = evt.target.files;
    var file = files[0];

    if (files && file) {
        var reader = new FileReader();

        reader.onload = function (readerEvt) {
            var binaryString = readerEvt.target.result;
            b64image = btoa(binaryString);
            content_type = file['type'];
            new_img_64b = 'data:' + content_type + ';base64,' + b64image;

            $('#id_profile_photo').css("background-image", "url('" + new_img_64b.replace(/(\r\n|\n|\r)/gm, "") + "')");
        };

        reader.readAsBinaryString(file);
    }
};

$('#id_personal_email').focusout(function () {
    personal_email_validate();
});
$('#id_personal_email').focusin(function () {
    $('#id_personal_email_errors').css('display', 'none');
    $('input#id_personal_email').css('border', '1px solid #CCC');
});

$('#id_facebook_profile').focusout(function () {
    facebook_profile_validate();
});
$('#id_facebook_profile').focusin(function () {
    $('#id_facebook_profile_errors').css('display', 'none');
    $('input#id_facebook_profile').css('border', '1px solid #CCC');
});

$('#id_google_profile').focusout(function () {
    google_profile_validate();
});
$('#id_google_profile').focusin(function () {
    $('#id_google_profile_errors').css('display', 'none');
    $('input#id_google_profile').css('border', '1px solid #CCC');
});

$('#id_twitter_profile').focusout(function () {
    twitter_profile_validate();
});
$('#id_twitter_profile').focusin(function () {
    $('#id_twitter_profile_errors').css('display', 'none');
    $('input#id_twitter_profile').css('border', '1px solid #CCC');
});

$('#id_linkedin_profile').focusout(function () {
    linkedin_profile_validate();
});
$('#id_linkedin_profile').focusin(function () {
    $('#id_linkedin_profile_errors').css('display', 'none');
    $('input#id_linkedin_profile').css('border', '1px solid #CCC');
});

$('#id_homepage').focusout(function () {
    homepage_validate();
});
$('#id_homepage').focusin(function () {
    $('#id_homepage_errors').css('display', 'none');
    $('input#id_homepage').css('border', '1px solid #CCC');
});

function scrollIntoView(eleID) {
    var e = document.getElementById(eleID);
    if (!!e && e.scrollIntoView) {
        e.scrollIntoView(false);
    }
}

function hasError(id) {
    if ($('#' + id).is(':visible')) {
        console.log(id + "is visible")
        scrollIntoView(id);
        return true;
    }
    return false;
}

function nextButtonClicked() {

    personal_email_validate();
    facebook_profile_validate();
    google_profile_validate();
    twitter_profile_validate();
    linkedin_profile_validate();
    homepage_validate();

    if (hasError('id_personal_email_errors')
        //||  hasError('id_gender_errors')
        //||  hasError('id_marital_status_errors')
        || hasError('id_linkedin_profile_errors')
        || hasError('id_facebook_profile_errors')
        || hasError('id_google_profile_errors')
        || hasError('id_google_profile_errors')
        || hasError('id_homepage_errors')
    //||  hasError('id_email_errors')
        ) {
        return;
    }

    full_user_data['objects'][0]['personal_email'] = $('input#id_personal_email').val();
    full_user_data['objects'][0]['gender'] = $('select#id_gender').val();
    full_user_data['objects'][0]['marital_status'] = $('select#id_marital_status').val();
    full_user_data['objects'][0]['linkedin_profile'] = $('input#id_linkedin_profile').val();
    full_user_data['objects'][0]['facebook_profile'] = $('input#id_facebook_profile').val();
    full_user_data['objects'][0]['google_profile'] = $('input#id_google_profile').val();
    full_user_data['objects'][0]['twitter_profile'] = $('input#id_twitter_profile').val();
    full_user_data['objects'][0]['homepage'] = $('input#id_homepage').val();
    if (full_user_data['objects'][0]['current_location'] == null) {
        full_user_data['objects'][0]['current_location'] = {
            'city': null,
            'country': {
                name: null
            }

        }
    }
    full_user_data['objects'][0]['current_location']['city'] = $('select#id_city').val();
    full_user_data['objects'][0]['current_location']['country']['name'] = $('select#id_country').text();

    var img = document.getElementById("id_profile_photo").style.backgroundImage;
    if (img.endsWith('alumniportal/img/user.jpg')) {
        full_user_data['objects'][0]['profile_photo'] = null;
    }
    else {
        if (full_user_data['objects'][0]['profile_photo'] == null) {
            full_user_data['objects'][0]['profile_photo'] = {}
        }
        full_user_data['objects'][0]['profile_photo']['content_type'] = img.substring(8, img.indexOf(';'));
        full_user_data['objects'][0]['profile_photo']['file'] = img.substring(img.indexOf(',') + 1, img.length - 1);
        full_user_data['objects'][0]['profile_photo']['name'] = full_user_data['objects'][0]['id'] + '.img';
    }

    saveProfileData(full_user_data, '/test/profile/edit/education/');
}

$(document).ready(function () {
    // change the number in the line below to change current progress on the progress bar
    $('div.checkout-wrap ul.checkout-bar li:nth-child(2)').addClass('active');
    // adding class "visited" to all nodes before current active progress
    $('div.checkout-wrap ul.checkout-bar li:nth-child(1)').addClass('visited');
    document.getElementById('id_profile_photo_input').addEventListener('change', handleFileSelect, false);
    fetchCountryList(set_country_data, populateCountrySelectList);
    fetchCityList(set_city_data, populateCitySelectList);
    fetchProfileData(set_user_data, populateUserData);
    $('#id_profile_photo_change').css('opacity', '0');
    $('#id_profile_photo_change').mouseenter(function () {
        $('#id_profile_photo_change').css('opacity', '1');
    });
    $('#id_profile_photo_change').mouseleave(function () {
        $('#id_profile_photo_change').css('opacity', '0');
    });
    $('#id_profile_photo_change>div>span:first-child').mouseenter(function () {
        $(this).css('color', 'white')
    });
    $('#id_profile_photo_change>div>span:first-child').mouseleave(function () {
        $(this).css('color', '#CCC')
    });
    $('#id_profile_photo_change>div>span:last-child').mouseenter(function () {
        $(this).css('color', 'red')
    });
    $('#id_profile_photo_change>div>span:last-child').mouseleave(function () {
        $(this).css('color', '#CCC')
    });
    $('#id_profile_photo_change>div>span:first-child').click(function () {
        $('#id_profile_photo_input').click();
    });
    $('#id_profile_photo_change>div>span:last-child').click(function () {
        $('#id_profile_photo').css('background-image', 'url({{ STATIC_URL }}alumniportal/img/user.jpg)');
        new_img_64b = "";
    });
});