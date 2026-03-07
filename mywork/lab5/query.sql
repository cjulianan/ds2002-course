USE fvd6wy_db;
SELECT students.student_first_name, students.student_last_name, teachers.teacher_first_name, teachers.teacher_last_name FROM students JOIN teachers ON students.teacher_id = teachers.teacher_id WHERE students.student_last_name LIKE LOWER('%t%');
