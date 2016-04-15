var logged = false;
// Navbar

$(document).ready(function(){
    // Activate Carousel
    $("#myCarousel").carousel({interval: 5000, wrap: true, pause: false});
    // hide logged info
    $(".logged").hide();
    // hide login fields in the modal
    $(".login-field").hide();
    // hide the correspondent controls (either mobile or desktop)
});

function selectControls(){
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

window.addEventListener('resize', function(){selectControls()}, true);

$(".login-link").click(function( event ){
    $(".signup-field").hide();
    $(".login-field").show();
});

$(".signup-link").click(function( event ){
    $(".signup-field").show();
    $(".login-field").hide();
});

$(".login").click(function( event ) {
    logged = true;
    selectControls();
});

$(".sign-out").click(function( event ) {
    logged = false;
    selectControls();
});

// Search bar
dropChosen = false;

function dropdown(val){
    //change dropdown btn contents
    var y = document.getElementsByClassName('btn btn-default dropdown-toggle');
    y[0].style.backgroundColor = 'rgb(241,241,241)';
    switch(val){
        case 1: y[0].innerHTML = '<i class="fa fa-ticket fa-lg fa-fw"></i> <span class="caret"></span>'; break;
        case 2: y[0].innerHTML = '<img src="img/theater.png" style="width:18px">  &nbsp;<span class="caret"></span>'; break;
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
}, 500);
