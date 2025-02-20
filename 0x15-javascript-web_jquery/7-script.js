// Fetch the character name from the Star Wars API and display it in #character

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    $('#character').text(data.name);
});
