BEGIN;
CREATE TABLE "firm" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "name" varchar(100) NOT NULL
)
;
CREATE TABLE "season" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "year" varchar(20) NOT NULL,
    "is_active" bool
)
;
CREATE TABLE "teacher" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "first_name" varchar(50) NOT NULL,
    "middle_name" varchar(50),
    "last_name" varchar(50) NOT NULL,
    "firm_id" varchar(36) REFERENCES "firm" ("id")
)
;
CREATE TABLE "mentor" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "season_id" varchar(36) REFERENCES "season" ("id"),
    "teacher_id" varchar(36) REFERENCES "teacher" ("id")
)
;
CREATE TABLE "referee" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "season_id" varchar(36) REFERENCES "season" ("id"),
    "teacher_id" varchar(36) REFERENCES "teacher" ("id"),
    "email" varchar(254) NOT NULL
)
;
CREATE TABLE "referal" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "file" varchar(100),
    "referee_id" varchar(36) REFERENCES "referee" ("id")
)
;
CREATE TABLE "topic" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "season_id" varchar(36) REFERENCES "season" ("id"),
    "title" varchar(100) NOT NULL,
    "description" text NOT NULL,
    "mentor_id" varchar(36) REFERENCES "mentor" ("id"),
    "referee_id" varchar(36) REFERENCES "referee" ("id")
)
;
CREATE TABLE "comission_members_of_comission" (
    "id" integer NOT NULL PRIMARY KEY,
    "comission_id" varchar(36) NOT NULL,
    "teacher_id" varchar(36) NOT NULL REFERENCES "teacher" ("id"),
    UNIQUE ("comission_id", "teacher_id")
)
;
CREATE TABLE "comission" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "season_id" varchar(36) REFERENCES "season" ("id"),
    "start_time" datetime,
    "head_of_comission_id" varchar(36) UNIQUE REFERENCES "teacher" ("id")
)
;
CREATE TABLE "specialization" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "name" varchar(100) NOT NULL
)
;
CREATE TABLE "class_letter" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "letter" varchar(100) NOT NULL
)
;
CREATE TABLE "student" (
    "id" varchar(36) NOT NULL PRIMARY KEY,
    "is_deleted" bool NOT NULL,
    "season_id" varchar(36) REFERENCES "season" ("id"),
    "first_name" varchar(50) NOT NULL,
    "middle_name" varchar(50),
    "last_name" varchar(50) NOT NULL,
    "grade" real NOT NULL,
    "class_letter_id" varchar(36) REFERENCES "class_letter" ("id"),
    "specialization_id" varchar(36) REFERENCES "specialization" ("id"),
    "topic_id" varchar(36) REFERENCES "topic" ("id"),
    "mentor_id" varchar(36) REFERENCES "mentor" ("id"),
    "comission_id" varchar(36) REFERENCES "comission" ("id"),
    "referee_id" varchar(36) REFERENCES "referee" ("id")
)
;

COMMIT;
