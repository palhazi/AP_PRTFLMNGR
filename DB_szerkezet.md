*user*

- id (Primary Key, INTEGER)
- email (Unique, VARCHAR(150))
- password (VARCHAR(150))
- first_name (VARCHAR(150))
- second_name (VARCHAR(150))
- is_approved (BOOLEAN)

*Account*

AccountID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
AccountType (VARCHAR) --  új oszlop a fiók típusának meghatározására (pl. "Regular" vagy "Main")
InstrumentType (VARCHAR)
Maturity (DATE)
NominalValue (DECIMAL)
InterestConditions (VARCHAR)
DueInterest (DECIMAL)
DueInterestDate (DATE)


*asset*

- id (Primary Key, INTEGER)
- UserID (Foreign Key references user.id, INTEGER)
- asset_type (VARCHAR(100)) 
- name (VARCHAR(100)) 
- long_name (VARCHAR(250)) 
- description (TEXT) 
- location (VARCHAR(100)) 
- link (VARCHAR(200)) 
- costs (FLOAT) 
- additional_columns 

*note*

- id (Primary Key, INTEGER)
- data (VARCHAR(10000))
- date (DATETIME)
- user_id (Foreign Key references user.id, INTEGER)

*investment*

- id (Primary Key, INTEGER)
- UserID (Foreign Key references user.id, INTEGER)
- asset_id (Foreign Key references asset.id, INTEGER) -- new foreign key to link to the consolidated asset table
- asset_name (VARCHAR(150))
- asset_type (VARCHAR(150))
- purchase_date (DATETIME)
- purchase_price (FLOAT)
- quantity (FLOAT)
- current_price (FLOAT)
- expected_interest_amount (FLOAT)

Az adatbázis szerkezet a következő kapcsolatokkal rendelkezik:

*A "user" tábla kapcsolódik a következő táblákhoz:*

- "Accounts" tábla: A "user" tábla "id" oszlopa a "Accounts" tábla "UserID" oszlopával van kapcsolatban.
- "MainAccounts" tábla: A "user" tábla "id" oszlopa a "MainAccounts" tábla "UserID" oszlopával van

kapcsolatban.
- "asset" tábla: A "user" tábla "id" oszlopa a "asset" tábla "UserID" oszlopával van kapcsolatban.
- "note" tábla: A "user" tábla "id" oszlopa a "note" tábla "user_id" oszlopával van kapcsolatban.
- "investment" tábla: A "user" tábla "id" oszlopa a "investment" tábla "user_id" oszlopával van kapcsolatban.

*A "asset" tábla kapcsolódik a következő táblákhoz:*

- "investment" tábla: Az "asset" tábla "id" oszlopa a "investment" tábla "asset_id" oszlopával van kapcsolatban.

