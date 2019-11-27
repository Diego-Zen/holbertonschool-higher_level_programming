-- Lists all shows that have at least one genre linked
SELECT ts.title, tsg.genre_id
FROM tv_show_genres tsg
INNER JOIN tv_shows AS ts ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id ASC;
