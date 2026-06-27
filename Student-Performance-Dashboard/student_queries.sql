SELECT *
FROM students
LIMIT 5;

SELECT COUNT(*) AS Total_Students
FROM students;

SELECT
ROUND(AVG(math_score),2) AS Math,
ROUND(AVG(reading_score),2) AS Reading,
ROUND(AVG(writing_score),2) AS Writing
FROM students;

SELECT
status,
COUNT(*) AS Students
FROM students
GROUP BY status;


SELECT
performance_level,
COUNT(*) AS Students
FROM students
GROUP BY performance_level
ORDER BY Students DESC;

SELECT
gender,
COUNT(*) AS Students
FROM students
GROUP BY gender;

SELECT
gender,
ROUND(AVG(average_score),2) AS AvgScore
FROM students
GROUP BY gender;

SELECT
lunch,
ROUND(AVG(average_score),2) AS AvgScore
FROM students
GROUP BY lunch;

SELECT
test_preparation_course,
ROUND(AVG(average_score),2) AS AvgScore
FROM students
GROUP BY test_preparation_course;

SELECT
parental_level_of_education,
ROUND(AVG(average_score),2) AS AvgScore
FROM students
GROUP BY parental_level_of_education
ORDER BY AvgScore DESC;

SELECT
ROWID,
gender,
total_score
FROM students
ORDER BY total_score DESC
LIMIT 10;
