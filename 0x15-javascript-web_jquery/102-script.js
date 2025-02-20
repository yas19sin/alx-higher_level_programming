// Fetch and display translated "Hello" in DIV#hello when clicking the translate button

$(document).ready(() => {
    $('#btn_translate').click(() => {
        const lang = $('#language_code').val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
            $('#hello').text(data.hello);
        });
    });
});
