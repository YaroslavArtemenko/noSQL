CREATE KEYSPACE IF NOT EXISTS labwork1 WITH replication = {
	'class': 'SimpleStrategy',
	'replication_factor': '1'
};

CREATE TYPE IF NOT EXISTS labwork1.people_name_type(
	firstname text,
	lastname text
);


CREATE TABLE IF NOT EXISTS labwork1."People_Event_Contest"(
	people_name frozen<labwork1.people_name_type>,
	people_phone  LIST<frozen<SET<text>>>,
	people_email text,
	people_birthday text,
	
	event_name text,
	event_date timestamp,
	
	contest_name text,
	
	PRIMARY KEY ((people_email), event_name, contest_name)
);


CREATE TABLE IF NOT EXISTS labwork1."Event_Place"(
	event_name text,
	event_date timestamp,
	
	place_name text,
	place_adress text,
	place_count int STATIC,
	
	PRIMARY KEY (event_name, place_name)
);


CREATE INDEX e_name on labwork1."People_Event_Contest"(event_name);
CREATE INDEX p_adress on labwork1."Event_Place"(place_adress);
