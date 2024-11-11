SELECT
    (COUNT(*) FILTER (WHERE location = 'Germany' AND email_provider = 'gmail.com') * 100.0) /
    COUNT(*) AS percentage
FROM users;

WITH ranked_countries AS (
    SELECT
        location,
        COUNT(*) AS gmail_users_count,
        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rank
    FROM users
    WHERE email_provider = 'gmail.com'
    GROUP BY location
)
SELECT location, gmail_users_count
FROM ranked_countries
WHERE rank <= 3;


SELECT
    COUNT(*) AS gmail_users_over_60
FROM users
WHERE email_provider = 'gmail.com'
    AND CAST(SUBSTR(age_group, 2, INSTR(age_group, '-') - 2) AS INTEGER) >= 60;

