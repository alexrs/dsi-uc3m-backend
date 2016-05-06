var dropChosen = false; // states whether a category has been selected

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
