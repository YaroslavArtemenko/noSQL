	/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     23.10.2019 21:44:16                          */
/*==============================================================*/

/*
drop index "One Event Has Many Contests_FK";

drop index Contest_PK;

drop table Contest;

drop index "People Have Many Events_FK";

drop index Event_PK;

drop table Event;

drop index "Event Have Places2_FK";

drop index "Event Have Places_FK";

drop index "Event Have Places_PK";

drop table Event_have_Places;

drop index People_PK;

drop table People;

drop index Place_PK;

drop table Place;
*/

/*==============================================================*/
/* Table: Contest                                               */
/*==============================================================*/
create table Contest (
   contest_name         VARCHAR(20)          not null,
   event_name           VARCHAR(20)          null,
   constraint PK_CONTEST primary key (contest_name)
);

/*==============================================================*/
/* Index: Contest_PK                                            */
/*==============================================================*/
create unique index Contest_PK on Contest (
contest_name
);

/*==============================================================*/
/* Index: "One Event Has Many Contests_FK"                      */
/*==============================================================*/
create  index "One Event Has Many Contests_FK" on Contest (
event_name
);

/*==============================================================*/
/* Table: Event                                                 */
/*==============================================================*/
create table Event (
   event_name           VARCHAR(20)          not null,
   people_email         VARCHAR(20)          null,
   event_date           DATE                 null,
   constraint PK_EVENT primary key (event_name)
);

/*==============================================================*/
/* Index: Event_PK                                              */
/*==============================================================*/
create unique index Event_PK on Event (
event_name
);

/*==============================================================*/
/* Index: "People Have Many Events_FK"                          */
/*==============================================================*/
create  index "People Have Many Events_FK" on Event (
people_email
);

/*==============================================================*/
/* Table: Event_have_Places                                     */
/*==============================================================*/
create table Event_have_Places (
   event_name           VARCHAR(20)          not null,
   place_name           VARCHAR(30)          not null,
   constraint PK_EVENT_HAVE_PLACES primary key (event_name, place_name)
);

/*==============================================================*/
/* Index: "Event Have Places_PK"                                */
/*==============================================================*/
create unique index "Event Have Places_PK" on Event_have_Places (
event_name,
place_name
);

/*==============================================================*/
/* Index: "Event Have Places_FK"                                */
/*==============================================================*/
create  index "Event Have Places_FK" on Event_have_Places (
event_name
);

/*==============================================================*/
/* Index: "Event Have Places2_FK"                               */
/*==============================================================*/
create  index "Event Have Places2_FK" on Event_have_Places (
place_name
);

/*==============================================================*/
/* Table: People                                                */
/*==============================================================*/
create table People (
   people_email         VARCHAR(20)          not null,
   people_name          VARCHAR(20)          null,
   people_phone         VARCHAR(20)          null,
   people_birthday      DATE                 null,
   constraint PK_PEOPLE primary key (people_email)
);

/*==============================================================*/
/* Index: People_PK                                             */
/*==============================================================*/
create unique index People_PK on People (
people_email
);

/*==============================================================*/
/* Table: Place                                                 */
/*==============================================================*/
create table Place (
   place_name           VARCHAR(20)          not null,
   place_adress         VARCHAR(50)          null,
   constraint PK_PLACE primary key (place_name)
);

/*==============================================================*/
/* Index: Place_PK                                              */
/*==============================================================*/
create unique index Place_PK on Place (
place_name
);

alter table Contest
   add constraint "FK_CONTEST_ONE EVENT_EVENT" foreign key (event_name)
      references Event (event_name)
      on delete restrict on update restrict;

alter table Event
   add constraint "FK_EVENT_ONE OF TH_PEOPLE" foreign key (people_email)
      references People (people_email)
      on delete restrict on update restrict;

alter table Event_have_Places
   add constraint "FK_EVENT_HA_ONE EVENT_EVENT" foreign key (event_name)
      references Event (event_name)
      on delete restrict on update restrict;

alter table Event_have_Places
   add constraint "FK_EVENT_HA_ONE EVENT_PLACE" foreign key (place_name)
      references Place (place_name)
      on delete restrict on update restrict;
