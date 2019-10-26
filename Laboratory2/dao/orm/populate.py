from dao.orm.model import *


# очистка всех таблиц
db.session.query(association).delete()
db.session.query(Contest).delete()
db.session.query(Event).delete()
db.session.query(People).delete()
db.session.query(Place).delete()


# # # создане объектов
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('aaa@gmail.com', 'aaa', '+47447474774', '1835-1-23');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('bbb@gmail.com', 'bbb', '+399489384334', '487-2-21');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('ccc@gmail.com', 'ccc', '+23232332323', '1637-6-23');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('ddd@gmail.com', 'ddd', '+39842349238492', '1-1-1');
#
# insert into People (people_email, people_name, people_phone, people_birthday) values ('eee@gmail.com', 'eee', '+304930432432', '1049-1-1');
#

aaa = People(people_email = 'aaa@gmail.com',
             people_name = 'aaa',
             people_phone = '+47447474774',
             people_birthday = "1835-01-23"
             )

bbb = People(people_email = 'bbb@gmail.com',
             people_name = 'bbb',
             people_phone = '+399489384334',
             people_birthday = '487-2-21'
             )

ccc = People(people_email = 'ccc@gmail.com',
             people_name = 'ccc',
             people_phone = '+23232332323',
             people_birthday = '1637-6-23'
            )

ddd = People(people_email = 'ddd@gmail.com',
             people_name = 'ddd',
             people_phone = '+39842349238492',
             people_birthday = '1-1-1'
            )

eee = People(people_email = 'eee@gmail.com',
             people_name = 'eee',
             people_phone = '+304930432432',
             people_birthday = '1049-1-1'
            )


# insert into Event (event_name, people_email, event_date) values ('mg', 'ddd@gmail.com', '1051-1-4');
#
# insert into Event (event_name, people_email, event_date) values ('christmas', 'bbb@gmail.com', '1619-3-8');
#
# insert into Event (event_name, people_email, event_date) values ('new year', 'aaa@gmail.com', '1994-12-2');
#
# insert into Event (event_name, people_email, event_date) values ('oktoberfest', 'ddd@gmail.com', '538-10-29');
#
# insert into Event (event_name, people_email, event_date) values ('football', 'ddd@gmail.com', '1-1-1');

mg = Event(event_name = 'mg',
           people_email = 'ddd@gmail.com',
           event_date = '1051-1-4')

christmas = Event(event_name = 'christmas',
                  people_email = 'bbb@gmail.com',
                  event_date = '1619-3-8'
                  )

new_year = Event(event_name = 'new year',
                 people_email = 'aaa@gmail.com',
                 event_date = '1994-12-2'
                 )

oktoberfest = Event(event_name = 'oktoberfest',
                    people_email = 'ddd@gmail.com',
                    event_date = '538-10-29'
                    )

football = Event(event_name = 'football',
                 people_email = 'ddd@gmail.com',
                 event_date = '1-1-1'
                 )


# insert into Place (place_name, place_adress) values ('museum', 'Киевская, Киев, Ковальський провулок, 5, 5-26');
#
# insert into Place (place_name, place_adress) values ('club', 'Hindenburgstraße 7a, 57072 Siegen');
#
# insert into Place (place_name, place_adress) values ('restaurant', 'Hindenburgstraße 12, 57072 Siegen');
#
# insert into Place (place_name, place_adress) values ('stadion', 'Leimbachstadion, Leimbachstraße 263, 57074 Siegen');
#
# insert into Place (place_name, place_adress) values ('theatre', 'Morleystraße 1, 57072 Siegen');

museum = Place(place_name = 'museum',
               place_adress = 'Киевская, Киев, Ковальський провулок, 5, 5-26'
               )

club = Place(place_name = 'club',
             place_adress = 'Hindenburgstraße 7a, 57072 Siegen'
             )

restaurant = Place(place_name = 'restaurant',
                   place_adress = 'Hindenburgstraße 12, 57072 Siegen'
                   )

stadion = Place(place_name = 'stadion',
                place_adress = 'Leimbachstadion, Leimbachstraße 263, 57074 Siegen'
                )

theatre = Place(place_name = 'theatre',
                place_adress = 'Morleystraße 1, 57072 Siegen')


# insert into Contest (contest_name, event_name) values ('bier', 'football');
#
# insert into Contest (contest_name, event_name) values ('present', 'new year');
#
# insert into Contest (contest_name, event_name) values ('speed', 'christmas');
#
# insert into Contest (contest_name, event_name) values ('bottle of wine', 'christmas');
#
# insert into Contest (contest_name, event_name) values ('bierpong', 'oktoberfest');

bier = Contest(contest_name = 'bier',
               event_name = 'football'
               )

present = Contest(contest_name = 'present',
                  event_name = 'new year'
                  )

speed = Contest(contest_name = 'speed',
                event_name = 'christmas'
                )

bottle_of_wine = Contest(contest_name = 'bottle of wine',
                         event_name = 'christmas'
                         )

bierpong = Contest(contest_name = 'bierpong',
                   event_name = 'oktoberfest'
                   )


ddd.people_event.append(mg)
bbb.people_event.append(christmas)
aaa.people_event.append(new_year)
ddd.people_event.append(oktoberfest)
ddd.people_event.append(football)

football.event_contest.append(bier)
new_year.event_contest.append(present)
christmas.event_contest.append(speed)
christmas.event_contest.append(bottle_of_wine)
oktoberfest.event_contest.append(bierpong)

mg.place_name_fk.append(museum)
christmas.place_name_fk.append(club)
new_year.place_name_fk.append(restaurant)
oktoberfest.place_name_fk.append(stadion)
football.place_name_fk.append(theatre)


db.session.add_all([aaa, bbb, ccc, ddd, eee,
                    mg, christmas, new_year, oktoberfest, football,
                    museum, club, restaurant, stadion, theatre,
                    bier, present, speed, bottle_of_wine, bierpong
])

db.session.commit()
