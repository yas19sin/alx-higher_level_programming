// Fetch all Star Wars movie titles and list them in UL#list_movies

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    data.results.forEach((movie) => {
        $('#list_movies').append(`<li>${movie.title}</li>`);
    });
});
