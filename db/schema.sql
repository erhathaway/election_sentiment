drop table if exists sources;
create table sources (
  id integer primary key autoincrement,
  name text not null,
  type text not null
);

drop table if exists canidate;
create table canidate (
  id integer primary key autoincrement,
  first_name text not null,
  last_name text not null,
  party text not null
);

drop table if exists article;
create table article (
  id integer primary key autoincrement,
  source_id integer not null,
  canidate_id integer not null,
  canidate_mention_count integer,
  url text not null,
  headline text not null,
  author_1 text not null,
  author_2 text,
  author_3 text,
  contents blob,
  publish_date numberic not null,
  scrape_status text not null,
  FOREIGN KEY(source_id) REFERENCES sources(id),
  FOREIGN KEY(canidate_id) REFERENCES canidate(id)
);

drop table if exists sentiment;
create table sentiment (
  id integer primary key autoincrement,
  score real not null,
  article_id integer not null,
  FOREIGN KEY(article_id) REFERENCES article(id)
);