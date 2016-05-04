var mail_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
var pwd_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
var name_regex = /^[a-zA-Z0-9]+$/;
var combo_regex = /^[a-zA-Z0-9@._]+$/;


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
function validate(num, id) {
    var tmp = document.getElementById(id).value;
    switch (num) {
        
        case 0://validate email
            var prnt = document.getElementById("sign-mail-div");
            var icn = document.getElementById("sign-mail-icon");
            if(tmp.match(mail_regex)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "sign-mail-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "sign-mail-feedback", "Correo inválido", prnt); 
            }
            break;
            
        case 1://validate username
            var prnt = document.getElementById("sign-usr-div");
            var icn = document.getElementById("sign-usr-icon");
            if(tmp.match(name_regex)){//set all ok
               switchFormState(1, prnt, icn);
                creatDelText(0, "sign-usr-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "sign-usr-feedback", "Nombre de usuario inválido", prnt); 
            }
            break;
            
        case 2://validate pwd
            var prnt = document.getElementById("sign-pwd-div");
            var icn = document.getElementById("sign-pwd-icon");
            if(tmp.match(pwd_regex)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "sign-pwd-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "sign-pwd-feedback", "Contraseña inválida: mínimo 8 caracteres, una mayúscula y un número", prnt); 
            }
            break;
            
        case 3://validate confirm pwd
            var prnt = document.getElementById("sign-pwd-confirm-div");
            var icn = document.getElementById("sign-pwd-confirm-icon");
            if(tmp.match(pwd_regex)){//set all ok
                var og_pwd = document.getElementById("sign-pwd").value;
                var zis_pwd = document.getElementById("sign-pwd-confirm").value;
                if(og_pwd == zis_pwd){
                    switchFormState(1, prnt, icn);
                    creatDelText(0, "sign-pwd-confirm-feedback", null, prnt);
                }
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "sign-pwd-confirm-feedback", "Las contraseñas no concuerdan", prnt); 
            }
            break;
    }
    formSendEnabler(0);
}



//Format validation for login form
function login(num, id){
    var tmp = document.getElementById(id).value;
    switch(num){
        case 0://validate email
            var prnt = document.getElementById("login-mail-div");
            var icn = document.getElementById("login-mail-icon");
            if(tmp.match(combo_regex)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "login-mail-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "login-mail-feedback", "Correo/usuario inválido", prnt);    
            }
            break;
            
        case 1://validate password
            var prnt = document.getElementById("login-pwd-div");
            var icn = document.getElementById("login-pwd-icon");
            if(tmp.match(pwd_regex)){//set all ok
                switchFormState(1, prnt, icn);
                creatDelText(0, "login-pwd-feedback", null, prnt);
            } else {//set all not ok
                switchFormState(0, prnt, icn);
                creatDelText(1, "login-pwd-feedback", "Contraseña inválida: mínimo 8 caracteres, una mayúscula y un número", prnt);          
            }
            break;
    }
    formSendEnabler(1);
}

//Checks whether all fields have been validated to activate send button
function formSendEnabler(num){
    switch(num){
        case 0://signup shit
            if($("#sign-mail-div").hasClass("has-success") && $("#sign-usr-div").hasClass("has-success") && $("#sign-pwd-div").hasClass("has-success") && $("#sign-pwd-confirm-div").hasClass("has-success")){
                $("signup-form-btn").prop("disabled", false);
            } else {
               $("signup-form-btn").prop("disabled", true); 
            }
            break;
        case 1://login shit
            if($("login-mail-div").hasClass("has-success") && $("login-pwd-div").hasClass("has-success")){
                $("login-form-btn").prop("disabled", false);
            } else {
                $("login-form-btn").prop("disabled", true);
            }
            break;
    }
}

//changes name of user in display
function changename(num){
    var dest = document.getElementById("user-name-link");
    switch(num){
        case 0://signup
            var name = document.getElementById("sign-usr").value;
            dest.innerHTML = name;
            break;
        case 1://login
            var name = document.getElementById("login-email").value;
            if(name.match(mail_regex)){//If mail inserted
                dest.innerHTML = "(insert name from db)";
            } else {//Otherwise 
                dest.innerHTML = name;
            }
            break;
    }
}


