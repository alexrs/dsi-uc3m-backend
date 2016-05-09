$(document).ready( function () {
    $(".card-input").hide()
    $(".paypal").hide()
});

function payWithCard () {
    $(".card-input").show()
    $(".paypal").hide()
};

function payWithPal () {
    $(".card-input").hide()
    $(".paypal").show()
};

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
