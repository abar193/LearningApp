create table if not exists student (
    id integer primary key autoincrement,
    name text not null,
    info text
);

create table if not exists course (
    id integer primary key autoincrement,
    sid integer,
    name text not null,
    info text,
FOREIGN KEY(sid) REFERENCES student(id)
);

create table if not exists lecture (
    id integer primary key autoincrement,
    cid integer,
    name text not null,
FOREIGN KEY(cid) REFERENCES course(id)
);

create table if not exists note (
    id integer primary key autoincrement,
    lid integer,
    question text not null,
    answer text not null,
FOREIGN KEY(lid) REFERENCES lecture(id)
);
