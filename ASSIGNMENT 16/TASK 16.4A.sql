-- Update a book’s availability to FALSE when borrowed.
USE librarydb;
UPDATE books
SET available = FALSE
WHERE book_id = 1;
SELECT book_id, title, author, 
       IF(available, 'TRUE', 'FALSE') AS available 
FROM books 
WHERE book_id = 1;