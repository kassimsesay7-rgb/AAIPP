USE librarydb;

INSERT INTO members (member_id, name, email, join_date)
VALUES
(1, 'John Doe', 'john@example.com', '2025-01-01'),
(2, 'Jane Smith', 'jane@example.com', '2025-02-10');

INSERT INTO books (book_id, title, author, available)
VALUES
(1, 'Harry Potter', 'J.K. Rowling', TRUE),
(2, 'Atomic Habits', 'James Clear', TRUE);

INSERT INTO loans (loan_id, member_id, book_id, loan_date, return_date)
VALUES
(1, 1, 1, '2025-03-10', NULL);
