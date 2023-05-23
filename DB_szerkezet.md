Az összes tábla tehát így néz ki:

*user*

id (Primary Key, INTEGER)
email (Unique, VARCHAR(150))
password (VARCHAR(150))
first_name (VARCHAR(150))
second_name (VARCHAR(150))
is_approved (BOOLEAN)

*Accounts*

AccountID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
InstrumentType (VARCHAR)
Maturity (DATE)
NominalValue (DECIMAL)
InterestConditions (VARCHAR)
DueInterest (DECIMAL)
DueInterestDate (DATE)

*MainAccounts*

MainAccountID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
InstrumentType (VARCHAR)
Maturity (DATE)
NominalValue (DECIMAL)
InterestConditions (VARCHAR)
DueInterest (DECIMAL)
DueInterestDate (DATE)

*Properties*

PropertyID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
PropertyAddress (VARCHAR)
PropertyType (VARCHAR)
Value1 (DECIMAL)
Value2 (DECIMAL)
Value3 (DECIMAL)
Value4 (DECIMAL)

*Coins*

CoinID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
CoinName (VARCHAR)
Theme (VARCHAR)
Status (VARCHAR)
PurchasePrice (DECIMAL)
CurrentPrice (DECIMAL)
Category (VARCHAR)
Condition (VARCHAR)
Type (VARCHAR)

*ETFs*

ETFID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
ETF (VARCHAR)
ETFName (VARCHAR)
Contents (TEXT)
Link (VARCHAR)
OngoingCharges (DECIMAL)
Broker (VARCHAR)

*Portfolio*

PortfolioID (Primary Key, INT)
UserID (Foreign Key references user.id, INT)
Instrument (VARCHAR)
Position (INT)
Last (DECIMAL)
CostBasis (DECIMAL)
MarketValue (VARCHAR)
AvgPrice (DECIMAL)

*note*

id (Primary Key, INTEGER)
data (VARCHAR(10000))
date (DATETIME)
user_id (Foreign Key references user.id, INTEGER)

*asset*

id (Primary Key, INTEGER)
name (VARCHAR(100))
long_name (VARCHAR(250))
type (VARCHAR(100))
interest_payment_date (DATE)
maturity_date (DATE)
description (TEXT)
location (VARCHAR(100))
link (VARCHAR(200))
costs (FLOAT)

*investment*

id (Primary Key, INTEGER)
asset_name (VARCHAR(150))
asset_type (VARCHAR(150))
purchase_date (DATETIME)
purchase_price (FLOAT)
quantity (FLOAT)
current_price (FLOAT)
expected_interest_amount (FLOAT)
user_id (INTEGER)
asset_id (INTEGER)

Az adatbázis szerkezet a következő kapcsolatokkal rendelkezik:

*A "user" tábla kapcsolódik a következő táblákhoz:*

"Accounts" tábla: A "user" tábla "id" oszlopa a "Accounts" tábla "UserID" oszlopával van kapcsolatban.

"MainAccounts" tábla: A "user" tábla "id" oszlopa a "MainAccounts" tábla "UserID" oszlopával van kapcsolatban.

"Properties" tábla: A "user" tábla "id" oszlopa a "Properties" tábla "UserID" oszlopával van kapcsolatban.

"Coins" tábla: A "user" tábla "id" oszlopa a "Coins" tábla "UserID" oszlopával van kapcsolatban.

"ETFs" tábla: A "user" tábla "id" oszlopa a "ETFs" tábla "UserID" oszlopával van kapcsolatban.

"Portfolio" tábla: A "user" tábla "id" oszlopa a "Portfolio" tábla "UserID" oszlopával van kapcsolatban.

"note" tábla: A "user" tábla "id" oszlopa a "note" tábla "user_id" oszlopával van kapcsolatban.

"investment" tábla: A "user" tábla "id" oszlopa a "investment" tábla "user_id" oszlopával van kapcsolatban.

*A "asset" tábla kapcsolódik a következő táblákhoz:*

"investment" tábla: Az "asset" tábla "id" oszlopa a "investment" tábla "asset_id" oszlopával van kapcsolatban.