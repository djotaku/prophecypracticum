DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS prophecy;

CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, supplicant_id INT, prophet_id INT, prophecy_given BIT, prophecy_received BIT, prophecy_received_and_interacted BIT, this_week_prophecy_id INT admin BIT DEFAULT 0);