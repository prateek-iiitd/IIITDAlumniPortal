/**
 * Created by ankur on 4/6/15.
 */
String.prototype.endsWith = function (suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
    //return this.indexOf(suffix) !== -1;
};

function fetchCountryList(fn_set_country_data, fn_populateCountrySelectList) {
    $.ajax({
        url: "/api/v1/country/?format=json",
        type: "GET",
        dataType: "json",
        success: function (response, status, xhr) {
            fn_set_country_data(response['objects']);
            fn_populateCountrySelectList();
        },
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}

function fetchCityList(fn_set_city_data ,fn_populateCitySelectList) {
    $.ajax({
        url: "/api/v1/city/?format=json",
        type: "GET",
        dataType: "json",
        success: function (response, status, xhr) {
            fn_set_city_data(response['objects']);
            fn_populateCitySelectList();
        },
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}

function fetchProfileData(fn_set_user_data , fn_populateUserData) {
    $.ajax({
        url: "/api/v1/current/?format=json",
        type: "GET",
        dataType: "json",
        success: function (response, status, xhr) {
            fn_set_user_data(response);
            fn_populateUserData();
        },
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}

function saveProfileData(full_user_data, next_page_url) {
    $.ajax({
        url: "/api/v1/current/",
        type: "PUT",
        data: JSON.stringify(full_user_data),
        dataType: "json",
        contentType: "application/json",
        processData: false,
        success: function (response, status, xhr) {
//            window.location.replace('/test/profile/edit/education/');
            window.location.replace(next_page_url);
        },
        error: function (xhr, status, error) {
            console.log(status + ' ' + error);
        }
    });
}