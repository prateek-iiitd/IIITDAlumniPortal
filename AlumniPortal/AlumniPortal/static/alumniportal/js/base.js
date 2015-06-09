/**
 * Created by sauhard on 30/8/14.
 */
/**
 * Created by sauhard on 29/8/14.
 */
$(document).ready(function () {
    if (document.URL=="http://127.0.0.1:8000/")
    {
        $("#nav-bar a:first-child li").css("color", "rgb(63, 173, 168)");
    }
    else if (document.URL=="http://127.0.0.1:8000/news/")
    {
        $("#nav-bar a:nth-child(2) li").css("color", "rgb(63, 173, 168)");
    }
    else if (document.URL=="http://127.0.0.1:8000/blog/")
    {
        $("#nav-bar a:nth-child(3) li").css("color", "rgb(63, 173, 168)");
    }
    else if (document.URL=="http://127.0.0.1:8000/directory/")
    {
        $("#nav-bar a:nth-child(4) li").css("color", "rgb(63, 173, 168)");
    }
    else if (document.URL=="http://127.0.0.1:8000/giveback/")
    {
        $("#nav-bar a:nth-child(5) li").css("color", "rgb(63, 173, 168)");
    }
    else if (document.URL=="http://127.0.0.1:8000/contact_us")
    {
        $("#nav-bar a:nth-child(6) li").css("color", "rgb(63, 173, 168)");
    }

    $("#openfeedback").click(function() {
        console.log("Clicking");
        $("#black").css("z-index", 999).fadeTo("medium", 0.7);
        $("#feedback").css("z-index", 1000).slideDown("fast");
//        $("#feedback").css("z-index", 1000).fadeTo("medium", 1);
    });
    var $close = function() {
        $("#black").fadeTo("medium", 0).css("z-index", -1);
        $("#feedback").slideUp("fast").css("z-index", -1);
    }
    $("#feedback #close").click(function () {
        $close();
    });
    $("#black").click(function () {
        $close();
    });
    $(document).keydown(function(e) {
    // ESCAPE key pressed
        if (e.keyCode == 27) {
            $close();
        }
    });

    $('#search-btn').mouseenter(function() {
        $('li.nav-search-box div.form-group span>span.glyphicon-search').css("color", "#3fada8");
    });
    $('#search-btn').mouseleave(function() {
        $('li.nav-search-box div.form-group span>span.glyphicon-search').css("color", "#555555");
    });
    $('#search-btn').click(function() {
        searchQuery = $('li.nav-search-box div.form-group input.form-control').val();
        console.log(searchQuery);
        window.location.href = '/test/prototype_result/?q='+searchQuery;
    });

    $('li.nav-search-box div.form-group input.form-control').keydown(function(e) {
    // ENTER key pressed
        if (e.keyCode == 13) {
            $('#search-btn').click();
        }
    });
});

function submitFeedbackForm()
{
    $.ajax({
            type: "POST",
            url: "/feedback/",
            data: $("#feedback>form").serialize(),
            success: function(data, textStatus, jqXHR){
                $("#feedback p").text("Thank you for your feedback!");
                $("#feedback form").slideUp("fast");
                $("#feedback").animate({height: "100px"});
                window.setTimeout($close, 2000);
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert("Error!")
            }
        }
    )
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}