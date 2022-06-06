CREATE TABLE IF NOT EXISTS "t_user" (
  "id" BIGSERIAL PRIMARY KEY,
  "author_id" BIGINT NOT NULL UNIQUE,
  "screen_name" varchar NOT NULL,
  "followers_count" bigint NOT NULL
);

CREATE TABLE IF NOT EXISTS "t_tweet" (
  "id" SERIAL PRIMARY KEY,
  "author_id" BIGINT,
  "text" text NOT NULL UNIQUE,
  "created_at" date NOT NULL
);

CREATE TABLE IF NOT EXISTS "t_hashtag" (
  "id" SERIAL PRIMARY KEY,
  "id_tweet" int,
  "hashtag" varchar NOT NULL
);

CREATE INDEX ON "t_user" ("followers_count");

CREATE INDEX ON "t_tweet" ("created_at");

CREATE INDEX ON "t_hashtag" ("hashtag");

ALTER TABLE "t_tweet" ADD FOREIGN KEY ("author_id") REFERENCES "t_user" ("author_id");

ALTER TABLE "t_hashtag" ADD FOREIGN KEY ("id_tweet") REFERENCES "t_tweet" ("id");