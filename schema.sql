
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS units;

-- =========================
-- STUDENTS TABLE
-- =========================
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- =========================
-- UNITS TABLE
-- =========================
CREATE TABLE units (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL
);

-- =========================
-- GRADES TABLE
-- =========================
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    unit_id INTEGER REFERENCES units(id) ON DELETE CASCADE,
    score INTEGER CHECK (score >= 0 AND score <= 100)
);

-- =========================

-- =========================
INSERT INTO students (name, email) VALUES
('Samuel Yotu', 'Samuel@example.com'),
('Jake Dwack', 'jake@example.com'),
('Alice Brown', 'alice+@example.com'),
('Brown Smith', 'brown@example.com'),
('Charlie Davinci', 'charlie@example.com'),
(' Wilson Smith', 'smith@example.com'),
('Eve White', 'eve@example.com'),
('Frank Harris', 'frank@example.com'),
('Grace kee', 'grace@example.com'),
('Harry King', 'harry@example.com');

-- =========================

-- =========================
INSERT INTO units (name, code) VALUES
('Computer Science', 'CS100'),
('Medicine', 'MED102'),
('Physics', 'PHY103'),
('Engineering', 'ENG104'),
('Information Technology', 'IT105');

-- =========================

-- =========================
INSERT INTO grades (student_id, unit_id, score) VALUES
(1, 1, 95),
(1, 2, 88),
(2, 1, 80),
(2, 3, 98),
(3, 2, 79),
(3, 4, 88),
(4, 1, 60),
(4, 5, 79),
(5, 3, 89),
(5, 2, 98),
(6, 4, 78),
(6, 1, 56),
(7, 5, 90),
(7, 2, 89),
(8, 3, 82),
(8, 4, 05),
(9, 1, 81),
(9, 5, 97),
(10, 2, 37),
(10, 3, 89);