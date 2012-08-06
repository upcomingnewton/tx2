function on_focus(id) {
    //alert("called");
    //alert();
    $('#' + id).css('border-color', 'blue');
}

function on_blur(id) {
    $('#' + id).css('border-color', '#cccccc');
    $('#' + id).css('color', 'black');
}