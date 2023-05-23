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