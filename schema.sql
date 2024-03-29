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

-- PROCEDURE: public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone)

-- DROP PROCEDURE IF EXISTS public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone);

CREATE OR REPLACE PROCEDURE public.insert_data(
	IN _student_name character varying,
	IN _student_email character varying,
	IN _student_grade character varying,
	IN _student_type_id integer,
	IN _exit_time timestamp with time zone)
LANGUAGE 'sql'

BEGIN ATOMIC
 INSERT INTO requests (student_name, student_email, student_grade, student_type_id, exit_time)
   VALUES (insert_data._student_name, insert_data._student_email, insert_data._student_grade, insert_data._student_type_id, insert_data._exit_time);
END;

ALTER PROCEDURE public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone)
    OWNER TO gp_admin;


-- PROCEDURE: public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying)

-- DROP PROCEDURE IF EXISTS public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying);

CREATE OR REPLACE PROCEDURE public.insert_data(
	IN _student_name character varying,
	IN _student_email character varying,
	IN _student_grade character varying,
	IN _student_type_id integer,
	IN _exit_time timestamp with time zone,
	IN _guardian_name character varying,
	IN _guardian_relation character varying,
	IN _guardian_email character varying,
	IN _reason character varying)
LANGUAGE 'sql'

BEGIN ATOMIC
 INSERT INTO requests (student_name, student_email, student_grade, student_type_id, exit_time)
   VALUES (insert_data._student_name, insert_data._student_email, insert_data._student_grade, insert_data._student_type_id, insert_data._exit_time);
END;

ALTER PROCEDURE public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying)
    OWNER TO gp_admin;

-- PROCEDURE: public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying)

-- DROP PROCEDURE IF EXISTS public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying);

CREATE OR REPLACE PROCEDURE public.insert_data(
	IN _student_name character varying,
	IN _student_email character varying,
	IN _student_grade character varying,
	IN _student_type_id integer,
	IN _exit_time timestamp with time zone,
	IN _guardian_name character varying,
	IN _guardian_relation character varying,
	IN _guardian_email character varying,
	IN _reason character varying)
LANGUAGE 'sql'

BEGIN ATOMIC
 INSERT INTO requests (student_name, student_email, student_grade, student_type_id, exit_time, guardian_name, guardian_relation, guardian_email, reason)
   VALUES (insert_data._student_name, insert_data._student_email, insert_data._student_grade, insert_data._student_type_id, insert_data._exit_time, insert_data._guardian_name, insert_data._guardian_relation, insert_data._guardian_email, insert_data._reason);
END;

ALTER PROCEDURE public.insert_data(character varying, character varying, character varying, integer, timestamp with time zone, character varying, character varying, character varying, character varying)
    OWNER TO gp_admin;


CREATE TABLE IF NOT EXISTS user_accounts (
  user_id SERIAL PRIMARY KEY, 
  username VARCHAR (50) UNIQUE NOT NULL, 
  password VARCHAR (100) NOT NULL, 
  email VARCHAR (100) UNIQUE NOT NULL, 
  created_at TIMESTAMP NOT NULL, 
  last_login TIMESTAMP
);

SELECT * FROM user_accounts

CREATE PROCEDURE register_user(username varchar, password varchar, email varchar)
LANGUAGE SQL
BEGIN ATOMIC
  INSERT INTO user_accounts(username, password, email) VALUES ('username', 'password', 'email');
END;


CREATE OR REPLACE PROCEDURE public.check_user(
	IN _password character varying,
	IN _email character varying,
    INOUT _val INT DEFAULT null)
LANGUAGE 'sql'

BEGIN ATOMIC
	SELECT COUNT(username) as val FROM public.user_accounts
	WHERE email =_email
	AND password =_password
	LIMIT 1;
END;

CREATE OR REPLACE PROCEDURE public.approve_request(
	IN _requestid integer,
    IN _approvedby varchar(100))
LANGUAGE 'sql'
AS $BODY$
	UPDATE requests 
	SET approved_by = _approvedby,
	approved_at = NOW() 
	WHERE request_id = _requestid;
$BODY$;
ALTER PROCEDURE public.approve_request(integer)
    OWNER TO gp_admin;


CREATE OR REPLACE FUNCTION get_todays_requests()
RETURNS TABLE (reqid INT,
			   stname VARCHAR, 
			   stemail VARCHAR,
			   stgrade VARCHAR,
			   sttypeid INT,
			   exittime TIMESTAMPTZ,
			   approvedby VARCHAR,
			   approvedat TIMESTAMPTZ,
			   createdat TIMESTAMPTZ,
			   updatedon TIMESTAMPTZ, 
			   gdname VARCHAR,
			   gdrelation VARCHAR,
			   gdemail VARCHAR,
			   reqreason VARCHAR)
LANGUAGE plpgsql
AS
$$
BEGIN
	RETURN QUERY
	SELECT
		request_id as reqid,
		student_name as stname,
		student_email as stemail,
		student_grade as stgrade,
		student_type_id as sttypeid,
		exit_time as exittime,
		approved_by as approvedby,
		approved_at as approvedat,
		request_created_at as createdat,
		request_updated_at as updatedon,
		guardian_name as gdname,
		guardian_relation as gdrelation,
		guardian_email as gdemail,
		reason as reqreason
	FROM
		requests
	WHERE
		DATE(exit_time) = CURRENT_DATE;
end;
$$;

-- FUNCTION: public.check_user(character varying)

-- DROP FUNCTION IF EXISTS public.check_user(character varying);

CREATE OR REPLACE FUNCTION public.check_user(
	_email character varying)
    RETURNS TABLE(useremail character varying, passwordhash character varying) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$
BEGIN
	RETURN QUERY
	SELECT
		email  as useremail,
		password as passwordhash
	FROM
		public.user_accounts
	WHERE
		email =_email;
end;
$BODY$;

ALTER FUNCTION public.check_user(character varying)
    OWNER TO gp_admin;
