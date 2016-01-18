
def up():
	DB.SQL('''CREATE TABLE dens (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);''')

	DB.SQL('''CREATE TABLE racers
		(racer_id 	INTEGER PRIMARY KEY AUTOINCREMENT,
		racer_name	TEXT	NOT NULL,
		racer_age	INT	NOT NULL,
		racer_den	INT	NOT NULL, 
		FOREIGN KEY(racer_den) REFERENCES dens(id));''')

	DB.SQL('''CREATE TABLE races
		(id 	INTEGER PRIMARY KEY AUTOINCREMENT);''')

	DB.SQL('''CREATE TABLE trials
		(id	INTEGER PRIMARY KEY AUTOINCREMENT, 
		racer_id	INTEGER,
		track		INTEGER,
		time		TEXT,
		race_id		INTEGER,
		FOREIGN KEY(racer_id) REFERENCES racers(racer_id),
		FOREIGN KEY(race_id) REFERENCES races(id));''')

def down():
	DB.SQL('''drop table dens''')
	DB.SQL('''drop table racers''')
	DB.SQL('''drop table races''')
	DB.SQL('''drop table trials''')
down()
up()
