$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function (response) {
            $.each(response.results, function (i, film) {
                $('UL#list_movies').append('<li>' + film.title + '</li>');
            });
        }
    });
});
