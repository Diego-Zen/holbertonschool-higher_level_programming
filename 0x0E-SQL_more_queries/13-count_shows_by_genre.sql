-- Lists all genres from 'hbtn_0d_tvshows and displays the number of shows linked to each'
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
GROUP BY genre
ORDER BY number_of_shows DESC;
