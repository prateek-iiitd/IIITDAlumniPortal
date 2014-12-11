/**
 * Created by sauhard on 10/11/14.
 */
$(document).ready(function(){
    if( document.URL.substr(-22) === "/admin_forms/add_news/" ) {
        $("#news-tab-panel-body").css("display", "block");
    }
    if( document.URL.substr(-23) === "/admin_forms/add_event/" ) {
        $("#event-tab-panel-body").css("display", "block");
    }
    if( document.URL.substr(-22) === "/admin_forms/add_blog/" ) {
        $("#blog-tab-panel-body").css("display", "block");
    }
    if( document.URL.substr(-27) === "/admin_forms/add_directory/" ) {
        $("#directory-tab-panel-body").css("display", "block");
    }
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