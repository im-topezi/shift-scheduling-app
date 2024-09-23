CREATE TABLE "shift_type" (
  "id" integer PRIMARY KEY,
  "description" varchar
);

CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar UNIQUE,
  "role" varchar
);

CREATE TABLE "roles" (
  "id" integer PRIMARY KEY,
  "description" varchar
);

CREATE TABLE "shifts" (
  "time_of_day" time,
  "day_of_week" varchar,
  "shift_type_id" integer,
  "shift_worker" integer,
  PRIMARY KEY ("time_of_day", "day_of_week")
);

ALTER TABLE "shifts" ADD FOREIGN KEY ("shift_type_id") REFERENCES "shift_type" ("id");

ALTER TABLE "shifts" ADD FOREIGN KEY ("shift_worker") REFERENCES "users" ("id");

ALTER TABLE "users" ADD FOREIGN KEY ("role") REFERENCES "roles" ("id");
