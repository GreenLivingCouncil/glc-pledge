create table pledges (
  id    integer not null primary key,
  name      text not null,
  sunetId   text not null,
  email     text not null,
  teamId       integer not null,
  eventId  integer not null,
  dateString   text not null,
  comments  text,
  referrer  text,
  private   integer not null default 1
);

create table teamCounts (
  id        integer not null primary key,
  eventId   integer not null,
  teamId    integer not null,
  count     integer not null default 0
);

create table referralCounts (
  referrer  text unique not null,
  count     integer not null default 0
);
  
  
