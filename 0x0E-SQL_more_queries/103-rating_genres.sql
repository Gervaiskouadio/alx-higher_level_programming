-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

--    Each record should display: tv_genres.name - rating sum
--    Results must be sorted in descending order by their rating
--    You can use only one SELECT statement
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows_rate ON tv_show_genres.tv_show_id = tv_shows_rate.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
