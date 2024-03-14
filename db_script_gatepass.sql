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

ALTER TABLE requests 
ALTER COLUMN exit_time TYPE TIMESTAMP WITH TIME ZONE;
ALTER COLUMN request_created_at TYPE TIMESTAMP WITH TIME ZONE;
ALTER COLUMN request_updated_at TYPE TIMESTAMP WITH TIME ZONE;
ALTER COLUMN approved_at TYPE TIMESTAMP WITH TIME ZONE;

CREATE PROCEDURE insert_data(_student_name VARCHAR(100), _student_email VARCHAR(100), _student_grade VARCHAR(2), _student_type_id INTEGER, _exit_time TIMESTAMP WITH TIME ZONE)
LANGUAGE SQL
BEGIN ATOMIC
  INSERT INTO requests(student_name, student_email, student_grade, student_type_id, exit_time)
  VALUES (_student_name, _student_email, _student_grade, _student_type_id, _exit_time);
END;

ALTER TABLE requests
ADD COLUMN guardian_name VARCHAR(100),
ADD COLUMN guardian_relation VARCHAR(100),
ADD COLUMN guardian_email VARCHAR(100);



CREATE TABLE parent (
	parent_id SERIAL NOT NULL PRIMARY KEY,
	primary_guardian_email VARCHAR(100) UNIQUE NOT NULL,
	secondary_guardian_email VARCHAR(100),
	primary_contactnumber VARCHAR(15) NOT NULL,
	seconday_contactnumber VARCHAR(15),
	createdon  TIMESTAMP DEFAULT now()
);
CREATE TABLE student (
	student_id SERIAL NOT NULL PRIMARY KEY,
	student_email VARCHAR(100) UNIQUE NOT NULL,
	student_grade VARCHAR(2) NOT NULL,
	student_type INT NOT NULL,
	parent_id int NOT NULL,
	createdon TIMESTAMP DEFAULT now()
)