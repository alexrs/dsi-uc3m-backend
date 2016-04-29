//Format validation for sign in form
function validate(id){
    var dummy_pwd;
    switch(id){
        case "sign-mail":
            var tmp = document.getElementById(id).value;
            if(tmp.match()){
                //if matching, display green tick in textbox
                document.getElementById();
            }
            else {
                //otherwise, provide error
                document.getElementById();
            }
            break;
        case "sign-usr":
            break;
        case "sign-pwd":
            break;
        case "sign-pwd-confirm":
            break;
    }
}