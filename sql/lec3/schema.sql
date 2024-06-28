CREATE TABLE collections (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "accession_number" TEXT NOT NULL UNIQUE,
    "acquired" NUMERIC,
    PRIMARY KEY("id")
);

CREATE TABLE "artists" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "created" (
    "artist_id" INTEGER,
    "collection_id" INTEGER,
    FOREIGN KEY("artist_id") REFERENCES "artists"("id") 
)
