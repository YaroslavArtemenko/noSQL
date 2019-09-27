INSERT INTO labwork1.People_Event_Contest (people_name, people_phone, people_email, people_birthday, event_name, event_date, contest_name) VALUES ({"firstname": 'qqq', "lastname": 'www'}, [{'0987654','0876554'}] , 'qqq@gmail.com', '11.11.11', 'prog', '1999-01-10 12:00', 'phone');
INSERT INTO labwork1.People_Event_Contest (people_name, people_phone, people_email, people_birthday, event_name, event_date, contest_name) VALUES ({"firstname": 'aaa', "lastname": 'bbb'}, [{'6565656','5757575'}] , 'aaa@gmail.com', '12.12.12', 'buhach', '2001-10-01 12:00', 'comp');
INSERT INTO labwork1.People_Event_Contest (people_name, people_phone, people_email, people_birthday, event_name, event_date, contest_name) VALUES ({"firstname": 'zzz', "lastname": 'xxx'}, [{'1212112','2434344'}] , 'zzz@gmail.com', '01.01.01', 'museum', '2002-11-09 13:00', 'money');

SELECT * FROM labwork1.People_Event_Contest;

INSERT INTO labwork1.Event_Place (event_name, event_date, place_name, place_adress, place_count) VALUES ('prog', '1999-01-10 12:00', 'ploscha', 'bulvar 1', 1);
INSERT INTO labwork1.Event_Place (event_name, event_date, place_name, place_adress, place_count) VALUES ('buhach', '2001-10-01 12:00', 'park', 'politech 1', 2);
INSERT INTO labwork1.Event_Place (event_name, event_date, place_name, place_adress, place_count) VALUES ('museum', '2002-11-09 13:00', 'park', 'politech 2', 3);

SELECT * FROM labwork1.Event_Place;

UPDATE labwork1.People_Event_Contest
SET 
	people_name={
					firstname: 'Updated',
					lastname: 'lastname'
				}
WHERE people_email = 'aaa@gmail.com' AND event_name = 'buhach' AND contest_name = 'comp' IF EXISTS;

SELECT * FROM labwork1.People_Event_Contest;


UPDATE labwork1.People_Event_Contest
SET people_birthday = 'UPDATED'
WHERE people_email = 'zzz@gmail.com' AND event_name = 'museum' AND contest_name = 'money' IF EXISTS;

SELECT * FROM labwork1.People_Event_Contest;


UPDATE labwork1.People_Event_Contest
SET people_phone = [{'Updated','0987654'}]
WHERE people_email = 'qqq@gmail.com' AND event_name = 'prog' AND contest_name = 'phone' IF EXISTS;

SELECT * FROM labwork1.People_Event_Contest;



UPDATE labwork1.Event_Place
SET place_adress = 'UPDATED'
WHERE event_name = 'buhach' AND place_name = 'park';

SELECT * FROM labwork1.Event_Place;

UPDATE labwork1.Event_Place
SET place_count = 2
WHERE event_name = 'museum';

SELECT * FROM labwork1.Event_Place;

UPDATE labwork1.Event_Place
SET event_date = '2001-10-01 13:00'
WHERE event_name = 'buhach' AND place_name = 'park';

SELECT * FROM labwork1.Event_Place;



DROP INDEX IF EXISTS e_name;
CREATE INDEX e_name on labwork1.People_Event_Contest(event_name);


SELECT people_name, event_name 
FROM labwork1.People_Event_Contest
WHERE event_name = 'buhach';


SELECT people_name, contest_name
FROM labwork1.People_Event_Contest
WHERE people_email = 'qqq@gmail.com';


SELECT event_name, contest_name
FROM labwork1.People_Event_Contest
WHERE  event_name = 'prog';


DROP INDEX IF EXISTS p_name;
CREATE INDEX p_adress on labwork1.Event_Place(place_adress);


SELECT event_name, place_adress
FROM labwork1.Event_Place
WHERE  place_adress = 'bulvar 1';



DELETE people_phone[0]
FROM labwork1.People_Event_Contest
WHERE people_email = 'aaa@gmail.com' AND event_name = 'buhach' AND contest_name = 'comp';

SELECT * FROM labwork1.People_Event_Contest;

DELETE people_birthday
FROM labwork1.People_Event_Contest
WHERE people_email = 'zzz@gmail.com' AND event_name = 'museum' AND contest_name = 'money';

SELECT * FROM labwork1.People_Event_Contest;

DELETE people_name
FROM labwork1.People_Event_Contest
WHERE people_email = 'qqq@gmail.com' AND event_name = 'prog' AND contest_name = 'phone';

SELECT * FROM labwork1.People_Event_Contest;


DELETE place_count 
FROM labwork1.Event_Place
WHERE event_name = 'buhach';

SELECT * FROM labwork1.Event_Place;

DELETE event_date
FROM labwork1.Event_Place
WHERE event_name = 'museum' AND place_name = 'park' ;

SELECT * FROM labwork1.Event_Place;

DELETE place_adress, place_count
FROM labwork1.Event_Place
WHERE event_name = 'prog' AND place_name = 'ploscha' ;

SELECT * FROM labwork1.Event_Place;

