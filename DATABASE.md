*Táblák exportálás*

létrehoz egy out.sql fájlt:

BEGIN TRANSACTION;
CREATE TABLE asset (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	long_name VARCHAR(250), 
	type VARCHAR(100) NOT NULL, 
	interest_payment_date DATE, 
	maturity_date DATE, 
	description TEXT, 
	location VARCHAR(100), 
	link VARCHAR(200), 
	costs FLOAT, 
	PRIMARY KEY (id)
);
INSERT INTO "asset" VALUES(1,'ETF','jgk9999999gkjgjkjgkjgkgjkgkgkgkgkgjg','iShares Automation Robotics','2023-05-13','2023-05-13','fdfdfdddfdsfdsfs','ibkr','',0.5);
INSERT INTO "asset" VALUES(2,'rtf',NULL,'iShares Automation Robotics','2023-05-16','2023-05-25','cdscsdcdcdcdd','Lightyear','https://www.justetf.com/en/etf-profile.html?query=IASP&groupField=index&from=search&isin=IE00B1FZS244#overview',0.5);
CREATE TABLE investment (
	id INTEGER NOT NULL, 
	asset_name VARCHAR(150), 
	asset_type VARCHAR(150), 
	purchase_date DATETIME, 
	purchase_price FLOAT, 
	quantity FLOAT, 
	current_price FLOAT, 
	expected_interest_amount FLOAT, 
	user_id INTEGER NOT NULL, 
	asset_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id) ON DELETE SET NULL, 
	FOREIGN KEY(asset_id) REFERENCES asset (id)
);
INSERT INTO "investment" VALUES(1,'ETF','iShares Automation Robotics','2023-05-18 00:00:00.000000',65464.0,5664.0,6456464.0,5646464.0,1,1);
INSERT INTO "investment" VALUES(2,'ETF','iShares Automation Robotics','2023-05-18 00:00:00.000000',456464646.0,456.0,1256.0,45646.0,1,1);
CREATE TABLE investment_snapshot (
	id INTEGER NOT NULL, 
	investment_id INTEGER, 
	snapshot_date DATETIME, 
	purchase_price FLOAT, 
	quantity FLOAT, 
	current_price FLOAT, 
	expected_interest_amount FLOAT, 
	snapshot_group_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(investment_id) REFERENCES investment (id)
);
INSERT INTO "investment_snapshot" VALUES(1,1,'2023-05-15 06:38:03.964229',65464.0,5664.0,6456464.0,5646464.0,1);
INSERT INTO "investment_snapshot" VALUES(2,1,'2023-05-16 05:48:29.409589',65464.0,5664.0,6456464.0,5646464.0,2);
INSERT INTO "investment_snapshot" VALUES(3,2,'2023-05-16 05:48:29.409589',456464646.0,456.0,1256.0,45646.0,2);
CREATE TABLE note (
	id INTEGER NOT NULL, 
	data VARCHAR(10000), 
	date DATETIME, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
INSERT INTO "note" VALUES(1,'dkldjéafdkséjfkdséfjkdédjkfdjdf','2023-05-14 11:29:37',1);
INSERT INTO "note" VALUES(2,'dsléfjséfjédsfjdséjfdséljf','2023-05-14 11:29:42',1);
INSERT INTO "note" VALUES(3,'jksskhskahskahsakash','2023-05-16 06:36:27',1);
CREATE TABLE user (
	id INTEGER NOT NULL, 
	email VARCHAR(150), 
	password VARCHAR(150), 
	first_name VARCHAR(150), 
	second_name VARCHAR(150), 
	is_approved BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO "user" VALUES(1,'palhazi.tamas@gmail.com','scrypt:32768:8:1$cMGTvrtldpazkNzd$d79880253423252004a5dd1a8ed24fda6a201dee491fb16af94b4e9d7c53cb8dfa650309e08197fd3b54b5be4cae6cf234185ee81d4c448c8b5b6c92498bf1eb','Pálházi','Tamás',1);
COMMIT;


*Táblák importlása*

input.sql kell legyen a munkakönyvtárban és azt importálja be

(base) palhazitamas@Palhazi-Mac-mini AP_PRTFLMNGR % sqlite3 '/Users/palhazitamas/Documents/A
P_PRTFLMNGR/instance/database.db' < input.sql
zsh: no such file or directory: input.sql