function selectSection(id) {
    $(".seat-section").removeClass( "selected-section" );
    switch(id) {
        case 0: $("#section-bl").addClass( "selected-section" ); break;
        case 1: $("#section-bm").addClass( "selected-section" ); break;
        case 2: $("#section-br").addClass( "selected-section" ); break;
        case 3: $("#section-mm").addClass( "selected-section" ); break;
        case 4: $("#section-fm").addClass( "selected-section" ); break;
    }
};
