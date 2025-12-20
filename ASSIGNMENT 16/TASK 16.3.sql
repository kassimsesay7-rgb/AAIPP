USE librarydb;
SELECT b.book_id, b.title, b.author, l.loan_date, l.return_date
FROM books b
JOIN loans l ON b.book_id = l.book_id
WHERE l.member_id = member_id;
