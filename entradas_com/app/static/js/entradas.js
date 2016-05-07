// global variables
var logged = false; //  states whether a user has already logged in


// Navbar user session buttons selection when resizing or loggin in/out
function selectControls(){
    // When mobile
    if ($(window).width() <= 767) {
        if (logged) {
            $(".login-option").hide();
            $(".desktop.logged").hide();
            $(".mobile.logged").show();
        } else {
            $(".logged").hide();
            $(".desktop.login-option").hide();
            $(".mobile.login-option").show();
        }
    // When desktop
    } else if ($(window).width() > 767){
        if (logged) {
            $(".login-option").hide();
            $(".mobile.logged").hide();
            $(".desktop.logged").show();
        } else {
            $(".logged").hide();
            $(".mobile.login-option").hide();
            $(".desktop.login-option").show();
        }
    }
}

// When opening the page, initializations
$(document).ready(function(){
    // Activate Carousel
    $("#header-carousel").carousel({interval: 5000, wrap: true, pause: false});
    // hide logged info
    $(".logged").hide();
    // hide login fields in the modal
    $(".login-field").hide();
    // hide the correspondent controls (either mobile or desktop)
    selectControls();
});

// When resizing the window, check if the
window.addEventListener('resize', function(){selectControls()}, true);

// When clicking in the login pill in the login/signup modal
$(".login-link").click(function( event ){
    // show the login form fields only
    $(".signup-field").hide();
    $(".login-field").show();
    // make the login pill active only
    $("#signup-tab").removeClass("active");
    $("#login-tab").addClass("active");
});

// When clicking in the signup pill in the login/signup modal
$(".signup-link").click(function( event ){
    // show the sign up form fields only
    $(".signup-field").show();
    $(".login-field").hide();
    // make the signup pill active only
    $("#login-tab").removeClass("active");
    $("#signup-tab").addClass("active");
});

// When clicking in the private area entering button
$(".login").click(function( event ) {
    logged = true;
    selectControls();
});

// When clicking in the private area exiting button
$(".sign-out").click(function( event ) {
    logged = false;
    selectControls();
});