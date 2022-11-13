
CREATE TABLE records.instrument (
                name VARCHAR NOT NULL,
                pitch VARCHAR NOT NULL,
                CONSTRAINT instrument_pk PRIMARY KEY (name)
);


CREATE TABLE records.address (
                addressID INTEGER NOT NULL,
                street1 VARCHAR(40) NOT NULL,
                street2 VARCHAR NOT NULL,
                number INTEGER NOT NULL,
                city VARCHAR NOT NULL,
                state VARCHAR NOT NULL,
                zipCode VARCHAR NOT NULL,
                telephone VARCHAR NOT NULL,
                CONSTRAINT address_pk PRIMARY KEY (addressID)
);


CREATE TABLE records.musician (
                ssn INTEGER NOT NULL,
                name VARCHAR(400) NOT NULL,
                addressID INTEGER NOT NULL,
                CONSTRAINT musician_pk PRIMARY KEY (ssn)
);


CREATE TABLE records.album (
                albumID INTEGER NOT NULL,
                title VARCHAR NOT NULL,
                release_date DATE NOT NULL,
                format VARCHAR NOT NULL,
                age INTEGER NOT NULL,
                ssn_producer INTEGER NOT NULL,
                CONSTRAINT album_pk PRIMARY KEY (albumID)
);


CREATE TABLE records.song (
                title VARCHAR NOT NULL,
                length INTEGER NOT NULL,
                ssn_author INTEGER NOT NULL,
                albumID INTEGER NOT NULL,
                CONSTRAINT song_pk PRIMARY KEY (title)
);


CREATE TABLE records.sounds (
                name VARCHAR NOT NULL,
                title VARCHAR NOT NULL,
                CONSTRAINT sounds_pk PRIMARY KEY (name, title)
);


CREATE TABLE records.performs (
                ssn INTEGER NOT NULL,
                title VARCHAR NOT NULL,
                CONSTRAINT performs_pk PRIMARY KEY (ssn, title)
);


CREATE TABLE records.plays (
                ssn INTEGER NOT NULL,
                name VARCHAR NOT NULL,
                CONSTRAINT plays_pk PRIMARY KEY (ssn, name)
);


ALTER TABLE records.plays ADD CONSTRAINT instrument_plays_fk
FOREIGN KEY (name)
REFERENCES records.instrument (name)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.sounds ADD CONSTRAINT instrument_sounds_fk
FOREIGN KEY (name)
REFERENCES records.instrument (name)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.musician ADD CONSTRAINT address_musician_fk
FOREIGN KEY (addressID)
REFERENCES records.address (addressID)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.performs ADD CONSTRAINT musician_plays_fk
FOREIGN KEY (ssn)
REFERENCES records.musician (ssn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.plays ADD CONSTRAINT musician_performs_fk
FOREIGN KEY (ssn)
REFERENCES records.musician (ssn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.song ADD CONSTRAINT musician_song_fk
FOREIGN KEY (ssn_author)
REFERENCES records.musician (ssn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.album ADD CONSTRAINT musician_album_fk
FOREIGN KEY (ssn_producer)
REFERENCES records.musician (ssn)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.song ADD CONSTRAINT album_song_fk
FOREIGN KEY (albumID)
REFERENCES records.album (albumID)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.performs ADD CONSTRAINT song_sounds_fk
FOREIGN KEY (title)
REFERENCES records.song (title)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE records.performs ADD CONSTRAINT song_performs_fk
FOREIGN KEY (title)
REFERENCES records.song (title)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;