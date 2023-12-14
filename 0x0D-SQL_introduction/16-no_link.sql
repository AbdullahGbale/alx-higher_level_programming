-- script that lists all records of the table second_table of hbtn_0c_0
SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL
ORDER BY score DESC;
