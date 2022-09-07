-- Import the database dump from hbtn_0d_tv_shows to your MYSQL server
-- A script that uses the hbtn_0d_tv_shows database to lists all genres of the show Dexter
-- Results must be sorted in ascending order by the genre name
SELECT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t
ON t.`id` = s.`show_id`
WHERE t.`title` = "Dexter"
ORDER BY g.`name`;
