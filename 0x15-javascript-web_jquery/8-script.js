$('#fetchMovies').click(function(){
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
        let movies = data.results;
        $('#list_movies').empty();
        $.each(movies, function(index, movie){
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    });
});