-- lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;