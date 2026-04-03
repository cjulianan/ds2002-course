USE fvd6wy_db;

INSERT INTO teachers (teacher_id, teacher_first_name, teacher_last_name, classroom_number) VALUES (11, 'Teacher', 'Eleven', 111);
INSERT INTO teachers (teacher_id, teacher_first_name, teacher_last_name, classroom_number) VALUES (12, 'Teacher', 'Twelve', 112);
INSERT INTO teachers (teacher_id, teacher_first_name, teacher_last_name, classroom_number) VALUES (13, 'Teacher', 'Thirteen', 113);

INSERT INTO students (student_id, student_first_name, student_last_name, teacher_id) VALUES (11, 'Student', 'Eleven', 11);
INSERT INTO students (student_id, student_first_name, student_last_name, teacher_id) VALUES (12, 'Student', 'Twelve', 12);
