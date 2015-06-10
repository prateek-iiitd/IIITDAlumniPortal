/**
 * Created by arch-it on 11/6/15.
 */

function profileSetupProgressBarEducation () {
    $('div.checkout-wrap ul.checkout-bar li:nth-child(2)').addClass('active');
    $('div.checkout-wrap ul.checkout-bar li:nth-child(1)').addClass('visited');
}

function initiateDatepicker (formSelector) {
    console.log(formSelector);

    $(formSelector+" .startDatepicker").datepicker({
        changeMonth: true,
        changeYear: true
    });

    $(formSelector+" .endDatepicker").datepicker({
        changeMonth: true,
        changeYear: true
    });
}

$(document).ready(function() {
    profileSetupProgressBarEducation();
    formSelector = "#form-0";
    initiateDatepicker(formSelector);
});

