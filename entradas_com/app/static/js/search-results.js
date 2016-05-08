$(document).ready(function () {
    dropdownFilter(0);
})

function dropdownFilter(val){
    //change dropdown btn contents
    var y = document.getElementsByClassName('btn btn-default dropdown-toggle filter-btn');
    y[0].style.backgroundColor = 'rgb(241,241,241)';
    switch(val){
        case 0: {
            y[0].innerHTML = '<span class="glyphicon glyphicon-map-marker"></span> &nbsp;<span class="caret"></span>';
            $("#filter-date").hide();
            $("#filter-location").show();
            break;
        }
        case 1: {
            y[0].innerHTML = '<span class="glyphicon glyphicon-calendar"></span>  &nbsp;<span class="caret"></span>';
            $("#filter-location").hide();
            $("#filter-date").show();
            break;
        }

    }
    dropChosen = true;
}
