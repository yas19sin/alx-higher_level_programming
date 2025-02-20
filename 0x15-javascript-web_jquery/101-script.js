// Add, remove, or clear list items when the user clicks on corresponding buttons

$(document).ready(() => {
    $('#add_item').click(() => $('.my_list').append('<li>Item</li>'));
    $('#remove_item').click(() => $('.my_list li:last').remove());
    $('#clear_list').click(() => $('.my_list').empty());
});
