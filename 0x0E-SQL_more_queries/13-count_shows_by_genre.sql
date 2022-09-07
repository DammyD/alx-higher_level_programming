-- Import the database dump from hbtn_0d_tv_shows to your MYSQL server
-- A script that lists all genres and dispalys the number of shows linked
-- Results must be sorted in descending order by the number of the shows linked
SELECT g.`name` AS `genre`,
COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t
ON g.`id` = t.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
