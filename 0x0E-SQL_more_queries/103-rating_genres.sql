-- Script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
    FROM tv_shows
    JOIN tv_show_ratings
        ON tv_shows.id = tv_show_ratings.show_id
    JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
    GROUP BY tv_genres.name
    ORDER BY rating DESC, tv_genres.name;
