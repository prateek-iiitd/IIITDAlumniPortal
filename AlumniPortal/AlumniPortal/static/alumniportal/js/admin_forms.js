/**
 * Created by sauhard on 10/11/14.
 */
$(document).ready(function(){
    $("#news-tab-panel-head").click(function() {
        $("#news-tab-panel-body").slideToggle("fast");
    });
    $("#event-tab-panel-head").click(function() {
        $("#event-tab-panel-body").slideToggle("fast");
    });
    $("#blog-tab-panel-head").click(function() {
        $("#blog-tab-panel-body").slideToggle("fast");
    });
    $("#directory-tab-panel-head").click(function() {
        $("#directory-tab-panel-body").slideToggle("fast");
    });
});