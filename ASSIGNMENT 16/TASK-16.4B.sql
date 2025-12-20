--delete a record from members table where member_id is 2  
DELETE m
FROM members m
LEFT JOIN loans l
    ON m.member_id = l.member_id AND l.return_date IS NULL
WHERE l.member_id IS NULL
  AND m.member_id = 2;
SELECT * FROM members;