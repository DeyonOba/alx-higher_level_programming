-- Script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show Dexter

SELECT DISTINCT tv_genres.name
    FROM tv_genres 
    JOIN tv_show_genres 
        ON tv_genres.id = tv_show_genres.genre_id 
    JOIN tv_shows 
        ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_genres.name NOT IN (
        SELECT DISTINCT tv_genres.name
            FROM tv_genres 
            JOIN tv_show_genres 
                ON tv_genres.id = tv_show_genres.genre_id 
            JOIN tv_shows 
                ON tv_shows.id = tv_show_genres.show_id
            WHERE tv_shows.title = 'Dexter'
    )
    ORDER BY tv_genres.name ASC;

-- Improving previous solution with CTE's

-- WITH genres AS (
--     SELECT tv_shows.title, tv_genres.name
--     FROM tv_genres 
--     JOIN tv_show_genres 
--         ON tv_genres.id = tv_show_genres.genre_id 
--     JOIN tv_shows 
--         ON tv_shows.id = tv_show_genres.show_id
-- ),
-- dexter_genre AS (
--     SELECT name
--     FROM genres
--     WHERE title = 'Dexter'
-- )

-- SELECT DISTINCT `name`
--     FROM genres
--     WHERE `name` NOT IN (SELECT * FROM dexter_genre)
--     ORDER BY `name`;

-- -- This solution has better readablity but uses more than 2 SELECT statement.