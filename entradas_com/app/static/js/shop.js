//controller for seating mechanism
function selectSection(id) {
    $(".seat-section").removeClass( "selected-section" );
    switch(id) {
        case 0: {
            if($("#section-bl").hasClass("available-section")) {
                $("#section-bl").addClass( "selected-section" );
            }
            break;
        }
        case 1: {
            if($("#section-bm").hasClass("available-section")) {
                $("#section-bm").addClass( "selected-section" );
            }
            break;
        }
        case 2: {
            if($("#section-br").hasClass("available-section")) {
                $("#section-br").addClass( "selected-section" );
            }
            break;
        }
        case 3: {
            if($("#section-mm").hasClass("available-section")) {
                $("#section-mm").addClass( "selected-section" );
            }
            break;
        }
        case 4: {
            if($("#section-fm").hasClass("available-section")) {
                $("#section-fm").addClass( "selected-section" );
            }
            break;
        }
    }
};

//regexes used to control forms in frontend
var mail_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
var card_number = /^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$/;
var card_month = /^(0?[1-9]|1[012])$/;
var card_year = /^\d{4}$/;

//Switches visual state of forms between error (0) and ok (1)
function switchFormState(state, prnt, icn){
    switch(state){//choose state
        case 0:
            prnt.classList.remove("has-warning");
            prnt.classList.remove("has-success");
            prnt.classList.add("has-error");
            icn.classList.remove("glyphicon-warning-sign");
            icn.classList.remove("glyphicon-ok");
            icn.classList.add("glyphicon-remove");
            break;
        case 1:
            prnt.classList.remove("has-warning");
            prnt.classList.remove("has-error");
            prnt.classList.add("has-success");
            icn.classList.remove("glyphicon-remove");
            icn.classList.remove("glyphicon-warning-sign");
            icn.classList.add("glyphicon-ok");
            break;
    }
}

//creates or deletes feedback text in forms
function creatDelText(state, identif, string, prnt){
    var bye = document.getElementById(identif);
    if(bye != null){
        bye.parentNode.removeChild(bye);
    }
    switch(state){
        case 0://delete
            break;
        case 1://create
            var info = document.createElement("P");
            info.style.color = "#a94442";
            info.id = identif;
            var txt = document.createTextNode(string);
            info.appendChild(txt);
            prnt.appendChild(info);
            break;         
    }      
}

//Format validation for sign in form
function cardcheck(num, id) {
    var tmp = document.getElementById(id).value;
    switch (num) {
        
        case 0://validate email
            var prnt = document.getElementById("shop-mail-div");
            var icn = document.getElementById("shop-mail-icon");
            if(tmp.match(mail_regex)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "shop-mail-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "sign-shop-feedback", "Correo inválido", prnt); 
            }
            break;
            
        case 1://validate card
            var prnt = document.getElementById("shop-card-div");
            var icn = document.getElementById("shop-card-icon");
            if(tmp.match(card_number)){//set all ok
               switchFormState(1, prnt, icn);
                creatDelText(0, "shop-card-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "shop-card-feedback", "Número de tarjeta inválido", prnt); 
            }
            break;
            
        case 2://validate month
            var prnt = document.getElementById("shop-month-div");
            var icn = document.getElementById("shop-month-icon");
            if(tmp.match(card_month)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "shop-month-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "shop-month-feedback", "Mes inválido, formato: mm", prnt); 
            }
            break;
            
        case 3://validate year
            var prnt = document.getElementById("shop-year-div");
            var icn = document.getElementById("shop-year-icon");
            if(tmp.match(card_year)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "shop-year-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "shop-year-feedback", "Año inválido, formato: yyyy", prnt); 
            }
            break;
         case 4://validate crc
            var prnt = document.getElementById("shop-crc-div");
            var icn = document.getElementById("shop-crc-icon");
            var crc = document.getElementById("shop-crr").value;
            if(crc >= 100 & <= 999){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "shop-crc-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "shop-crc-feedback", "CRC inválido, formato: nnn", prnt); 
            }
            break;
    }
    formSendEnabler(0);
}

//Checks whether all fields have been validated to activate send button
function enableSend(num){
    if(document.getElementById("shop-mail-div").classList.contains("has-success") && 
       document.getElementById("shop-card-div").classList.contains("has-success") &&
       document.getElementById("shop-month-div").classList.contains("has-success") &&
       document.getElementById("shop-year-div").classList.contains("has-success") &&
       document.getElementById("shop-crc-div").classList.contains("has-success")){

        document.getElementById("shop-form-btn").disabled = false;
    } else {
       document.getElementById("shop-form-btn").disabled = true;
    }
    break;
}