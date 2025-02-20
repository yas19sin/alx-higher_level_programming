// Fetch and display translated "Hello" when clicking the translate button or pressing ENTER

$(document).ready(() => {
    function translateHello() {
        const lang = $('#language_code').val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translateHello);

    $('#language_code').keypress((e) => {
        if (e.which === 13) { // Enter key
            translateHello();
        }
    });
});
