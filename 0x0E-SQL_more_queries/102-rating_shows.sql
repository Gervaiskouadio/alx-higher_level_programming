-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

--    Each record should display: tv_shows.title - rating sum
--    Results must be sorted in descending order by the rating
--    You can use only one SELECT statement
SELECT tv_shows.title, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
