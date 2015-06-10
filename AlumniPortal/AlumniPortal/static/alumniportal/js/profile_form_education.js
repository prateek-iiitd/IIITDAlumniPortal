/**
 * Created by Prateek on 10/06/15.
 */

//variables
var country_selectize;
var citySelectize;
var country_data;
var city_data;
var user_data = {};
var education_html;
var full_user_data = {};

function set_user_data(data) {
    full_user_data = data;
    user_data = full_user_data['objects'][0];

}

function set_city_data(data) {
    city_data = data;
}

function set_country_data(data) {
    country_data = data;
}

//Function to populate the HTML form with user data received from the API
function populateUserData() {
    console.log(user_data);
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


function fetchFormHtml() {
    $.ajax({
        url: STATIC_URL + "alumniportal/profile_form_education_form.html",
        type: "GET",
        dataType: "html",
        success: function (response, status, xhr) {
            education_html = response;
            console.log(education_html);
        },
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}

$(document).ready(function () {
    // change the number in the line below to change current progress on the progress bar
    $('div.checkout-wrap ul.checkout-bar li:nth-child(3)').addClass('active');
    // adding class "visited" to all nodes before current active progress
    $('div.checkout-wrap ul.checkout-bar li:nth-child(1)').addClass('visited');
    $('div.checkout-wrap ul.checkout-bar li:nth-child(2)').addClass('visited');

    $('#id_form-0-degree_type').selectize({
        create: true
    });

    fetchCountryList(set_country_data, populateCountrySelectList);
    fetchCityList(set_city_data, populateCitySelectList);
    fetchFormHtml();

    $('.selectize-input').css("position", "absolute");
    $('.selectize-control').css("position", "absolute");

    $(".btn-add").click(function () {
        $('form.input-form').html(education_html + $('form.input-form').html());
        $('.form:first-of-type').slideDown('medium');
        $('div.form div.row div.col-lg-1').on('click', 'span.glyphicon-remove', function () {
            $(this).parents('.form').slideUp('fast').addClass('deleted-form');
        });
    });
});