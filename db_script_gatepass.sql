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

CREATE TABLE IF NOT EXISTS guardian
(
    guardian_id integer NOT NULL DEFAULT nextval('parent_parent_id_seq'::regclass),
    primary_guardian_email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    secondary_guardian_email character varying(100) COLLATE pg_catalog."default",
    primary_contactnumber character varying(15) COLLATE pg_catalog."default" NOT NULL,
    seconday_contactnumber character varying(15) COLLATE pg_catalog."default",
    created_on timestamp without time zone DEFAULT now(),
    created_by character varying(100) COLLATE pg_catalog."default",
    student_list jsonb,
    CONSTRAINT parent_pkey PRIMARY KEY (guardian_id),
    CONSTRAINT parent_primary_guardian_email_key UNIQUE (primary_guardian_email)
)


CREATE TABLE student (
	student_id SERIAL NOT NULL PRIMARY KEY,
	student_email VARCHAR(100) UNIQUE NOT NULL,
	student_grade VARCHAR(2) NOT NULL,
	student_type INT NOT NULL,
	parent_id int NOT NULL,
	createdon TIMESTAMP DEFAULT now()
)

-- Alter TABLE public.guardian
-- ADD COLUMN student_list JSONB

-- PROCEDURE: public.profiledata(character varying, character varying, character varying, character varying, character varying)

-- DROP PROCEDURE IF EXISTS public.profiledata(character varying, character varying, character varying, character varying, character varying);

CREATE OR REPLACE PROCEDURE public.profiledata(
	IN _primary_guardian_email character varying,
	IN _primary_contactnumber character varying,
	IN _secondary_guardian_email character varying,
	IN _seconday_contactnumber character varying,
	IN _created_by character varying,
    IN _student_list jsonb)
LANGUAGE 'sql'
AS $BODY$
-- create or update profile data
 
   INSERT INTO public.guardian(primary_guardian_email,secondary_guardian_email
							,primary_contactnumber
							,seconday_contactnumber
							,created_by, student_list)
	values(_primary_guardian_email,_secondary_guardian_email
							,_primary_contactnumber
							,_seconday_contactnumber
		  					,_created_by,_student_list)

$BODY$;
ALTER PROCEDURE public.profiledata(character varying, character varying, character varying, character varying, character varying)
    OWNER TO gp_admin;


DROP FUNCTION profiledata
CREATE OR REPLACE FUNCTION public.profiledata(
	IN _guardian_id int,
	IN _primary_guardian_email character varying,
	IN _primary_contactnumber character varying,
	IN _secondary_guardian_email character varying,
	IN _seconday_contactnumber character varying,
	IN _created_by character varying,
    IN _student_list jsonb)
RETURNS 
TABLE(guardian_id integer,primary_guardian_email character varying
			  ,primary_contactnumber character varying,secondary_guardian_email character varying,seconday_contactnumber character varying,created_by character varying,student_list jsonb)
LANGUAGE 'plpgsql'
AS 
$$
begin
-- create or update profile data
IF guardianid = 0 then
   INSERT INTO public.guardian(primary_guardian_email,secondary_guardian_email
							,primary_contactnumber
							,seconday_contactnumber
							,created_by, student_list)
	values(_primary_guardian_email,_secondary_guardian_email
							,_primary_contactnumber
							,_seconday_contactnumber
		  					,_created_by,_student_list);

else
  UPDATE guardian
  SET secondary_guardian_email =_secondary_guardian_email
	,primary_contactnumber =_primary_contactnumber
	,seconday_contactnumber =_seconday_contactnumber
	,student_list =_student_list
  WHERE guardian_id = _guardian_id;
end if;


RETURN QUERY SELECT  
     guardian_id,
	 primary_guardian_email,
	 primary_contactnumber,
	 secondary_guardian_email,
	 seconday_contactnumber,
	 created_by,
     student_list
    FROM guardian
	WHERE primary_guardian_email = _primary_guardian_email
	LIMIT 1;
end;
$$;