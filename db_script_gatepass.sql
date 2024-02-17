CREATE TABLE student_type (
	student_type_id SERIAL NOT NULL PRIMARY KEY,
	student_type VARCHAR(20)
);

INSERT INTO student_type (student_type)
VALUES
	('Day Scholar'),
	('Weekly Boarder'),
	('Boarder');


CREATE TABLE requests (
	request_id SERIAL NOT NULL PRIMARY KEY,
	student_name VARCHAR(50),
	student_email VARCHAR(70),
	student_grade VARCHAR(2),
	student_type INT,
	exit_time TIMESTAMP,
	approved_by VARCHAR(50),
	approved_at TIMESTAMP DEFAULT NOW(),
	request_created_at TIMESTAMP DEFAULT NOW(),
	request_updated_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.request_updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION trigger_set_updated_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.request_updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_timestamp
BEFORE UPDATE ON requests
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_updated_timestamp();

CREATE TABLE approval_teachers (
	teacher_id SERIAL NOT NULL PRIMARY KEY,
	teacher_email VARCHAR(100) NOT NULL,
	student_type_id SERIAL REFERENCES student_type(student_type_id),
	student_grade VARCHAR(20), -- was defined as a VARCHAR and not an INT in the requests table, to fix?
	is_admin boolean DEFAULT FALSE,
	is_active boolean DEFAULT FALSE
);

INSERT INTO approval_teachers
VALUES
(1, 'example@example.com', 1, 11, TRUE, TRUE)

