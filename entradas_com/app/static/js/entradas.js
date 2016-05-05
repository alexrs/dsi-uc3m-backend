// global variables
var logged = false; //  states whether a user has already logged in
var dropChosen = false; // states whether a category has been selected

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

// Search bar dropdown function
function dropdown(val){
    //change dropdown btn contents
    var y = document.getElementsByClassName('btn btn-default dropdown-toggle');
    y[0].style.backgroundColor = 'rgb(241,241,241)';
    switch(val){
        case 1: y[0].innerHTML = '<i class="fa fa-ticket fa-lg fa-fw"></i> <span class="caret"></span>'; break;
        case 2: y[0].innerHTML = "<img src='{{ url_for('static', filename='img/theater.png') }}' style='width:18px''>  &nbsp;<span class='caret'></span>"; break;
        case 3: y[0].innerHTML = '<i class="fa fa-music fa-lg fa-fw"></i> <span class="caret"></span>'; break;
        case 4: y[0].innerHTML = '<i class="fa fa-university fa-lg fa-fw"></i> <span class="caret"></span>'; break;
        case 5: y[0].innerHTML = '<i class="fa fa-futbol-o fa-lg fa-fw"></i> <span class="caret"></span>'; break;
        case 6: y[0].innerHTML = '<i class="fa fa-magic fa-lg fa-fw" aria-hidden="true"></i> <span class="caret"></span>'; break;
        case 0: y[0].innerHTML = '<i class="fa fa-globe fa-lg fa-fw"></i> <span class="caret"></span>'; break;
    }
    dropChosen = true;
}

function setDefaultDrop(){
    dropChosen = true;
    var drop = document.getElementById('dropbtn');
    var searchbar = document.getElementsByClassName('form-control searchbar searchbar-text')[0];
    if (drop.innerHTML == '<i class="fa fa-question fa-lg fa-fw" aria-hidden="true"></i> <span class="caret"></span>'){
        drop.innerHTML = '<i class="fa fa-globe fa-lg fa-fw"></i> <span class="caret"></span>';
        drop.style.backgroundColor = 'rgb(241,241,241)';
    }
}

setInterval(function(){
    //get textbox and send form btn
    var searchbar = document.getElementsByClassName('form-control searchbar searchbar-text')[0];
    var searchbtn = document.getElementById('searchnow');
    //if dropdown has been chosen
    if (dropChosen === true){
       if(searchbar.value){
            //if not empty, shade line and if category chosen highlight btn
            searchbar.style.boxShadow= '0px 3px 0px rgb(241, 241, 241)';
            if(dropChosen){
                searchbtn.style.backgroundColor = 'rgb(255, 180, 2)';
            }
        }
        else{
            //if empty highlight line and remove color from btn
            searchbar.style.boxShadow= '0px 3px 0px rgb(255, 180, 2)';
            searchbtn.style.backgroundColor = 'rgb(241, 241, 241)';
        }
    }
}, 2000);
