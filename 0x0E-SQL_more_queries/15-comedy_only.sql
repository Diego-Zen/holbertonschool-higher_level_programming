-- Lists all comedy shows
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg ON tsg.show_id = ts.id
INNER JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
