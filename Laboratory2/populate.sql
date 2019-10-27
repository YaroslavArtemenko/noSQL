insert into People (people_email, people_name, people_phone, people_birthday) values ('aaa@gmail.com', 'aaa', '+47447474774', '1835-1-23');

insert into People (people_email, people_name, people_phone, people_birthday) values ('bbb@gmail.com', 'bbb', '+399489384334', '487-2-21');

insert into People (people_email, people_name, people_phone, people_birthday) values ('ccc@gmail.com', 'ccc', '+23232332323', '1637-6-23');

insert into People (people_email, people_name, people_phone, people_birthday) values ('ddd@gmail.com', 'ddd', '+39842349238492', '1-1-1');

insert into People (people_email, people_name, people_phone, people_birthday) values ('eee@gmail.com', 'eee', '+304930432432', '1049-1-1');

insert into Event (event_name, people_email, event_date) values ('mg', 'ddd@gmail.com', '1051-1-4');

insert into Event (event_name, people_email, event_date) values ('christmas', 'bbb@gmail.com', '1619-3-8');

insert into Event (event_name, people_email, event_date) values ('new year', 'aaa@gmail.com', '1994-12-2');

insert into Event (event_name, people_email, event_date) values ('oktoberfest', 'ddd@gmail.com', '538-10-29');

insert into Event (event_name, people_email, event_date) values ('football', 'ddd@gmail.com', '1-1-1');

insert into Place (place_name, place_adress) values ('museum', 'Киевская, Киев, Ковальський провулок, 5, 5-26');

insert into Place (place_name, place_adress) values ('club', 'Hindenburgstraße 7a, 57072 Siegen');

insert into Place (place_name, place_adress) values ('restaurant', 'Hindenburgstraße 12, 57072 Siegen');

insert into Place (place_name, place_adress) values ('stadion', 'Leimbachstadion, Leimbachstraße 263, 57074 Siegen');

insert into Place (place_name, place_adress) values ('theatre', 'Morleystraße 1, 57072 Siegen');

insert into Event_have_Places (event_name, place_name) values ('mg', 'museum');

insert into Event_have_Places (event_name, place_name) values ('christmas', 'club');

insert into Event_have_Places (event_name, place_name) values ('new year', 'restaurant');

insert into Event_have_Places (event_name, place_name) values ('oktoberfest', 'stadion');

insert into Event_have_Places (event_name, place_name) values ('football', 'theatre');

insert into Contest (contest_name, event_name) values ('bier', 'football');

insert into Contest (contest_name, event_name) values ('present', 'new year');

insert into Contest (contest_name, event_name) values ('speed', 'christmas');

insert into Contest (contest_name, event_name) values ('bottle of wine', 'christmas');

insert into Contest (contest_name, event_name) values ('bierpong', 'oktoberfest');
