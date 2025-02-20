// Fetch the "hello" translation for French and display it in DIV#hello

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data.hello);
});
