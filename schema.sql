CREATE TABLE "shift_type" (
  "id" SERIAL PRIMARY KEY,
  "description" varchar
);

CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "username" varchar UNIQUE,
  "role" integer
);

CREATE TABLE "roles" (
  "id" SERIAL PRIMARY KEY,
  "description" varchar UNIQUE
);

CREATE TABLE "shifts" (
  "time_of_day" time,
  "day_id" integer,
  "shift_type_id" integer,
  "shift_worker" integer,
  PRIMARY KEY ("time_of_day", "day_id")
);
CREATE TABLE "days" (
 "id" INTEGER PRIMARY KEY,
 "day_of_week" varchar
);


ALTER TABLE "shifts" ADD FOREIGN KEY ("shift_type_id") REFERENCES "shift_type" ("id");

ALTER TABLE "shifts" ADD FOREIGN KEY ("shift_worker") REFERENCES "users" ("id");

ALTER TABLE "users" ADD FOREIGN KEY ("role") REFERENCES "roles" ("id");

ALTER TABLE "shifts" ADD FOREIGN KEY ("day_id") REFERENCES "days" ("id");
