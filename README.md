1. **Dokumentáció**: Rendszeresen dokumentáld a kódodat, használj docstringeket a függvények és osztályok felett, 
valamint kommenteket a kód kritikus részeinél. Készíts egy `README.md` fájlt, 
amely tartalmazza az alkalmazás célját, az összetevőket, a telepítési és futtatási útmutatót.

2. **Kódstruktúra**: Tervezd meg a kódstruktúrát előre, és használj moduláris megközelítést 
a különféle összetevők elkülönítésére, például az adatbázis kezelő, 
a modell, az üzleti logika és a nézetek.

3. **Környezeti változók**: Használj környezeti változókat a konfigurációs beállítások tárolására, 
például az adatbázis kapcsolódási adatokhoz és az API kulcsokhoz. 
Ez lehetővé teszi, hogy az alkalmazás könnyen alkalmazkodjon a különböző környezetekhez, és biztonságosabb legyen.

4. **Verziókezelés**: Használj egy verziókezelő rendszert, például a Git-et a változások nyomon követésére 
és a kód fejlesztésének menedzselésére. Készíts ágakat a különböző fejlesztési szakaszokhoz, 
és használj pull requesteket a változások összefésülésére.

5. **Tesztelés**: Készíts automatizált teszteket az alkalmazás különböző részeihez. 
Ez lehetővé teszi, hogy biztosítsd az alkalmazás helyes működését a változtatások során.

6. **Hibakövetés**: Használj hibakövető eszközöket, mint például a Sentry vagy a Loggly, 
hogy könnyen azonosíthasd és javíthasd a futásidejű hibákat.

7. **Adatbázis migrációk**: Használj adatbázis migrációs eszközöket, 
mint például az Alembic-et, hogy kezeld az adatbázis sémaváltozásokat. 
Ez lehetővé teszi a változások visszavonását és előrehléptetését anélkül, hogy elveszítenéd az adatokat.

8. **Adatbázis kezelő**: Válassz egy megbízható adatbázis kezelőt, mint például SQLAlchemy 
vagy Django ORM, hogy egyszerűsítsd az adatbázis elérést és a tranzakciókezelést.

9. **Következetes kódstílus**: Tartsd be a PEP 8 kódolási szabályait, és használj automatikus formázó eszközöket, 
mint a Black vagy a flake8, hogy következetes kódstílust tarts fenn az egész projektben. 
Ez elősegíti a kód olvashatóságát és karbantarthatóságát.

10. **Konténerizáció és telepítés**: Fontolj meg egy konténerizációs megoldást, mint például a Docker, 
hogy egyszerűsítsd az alkalmazás telepítését és skálázását. Ezzel megkönnyíted a fejlesztőknek és az üzemeltetőknek 
az alkalmazás használatát és karbantartását.

Az **AP_PRTFLMNGR mappa** tartalmazza a következőket:

Icon: fájl
README.md: fájl
VSCODE.md: fájl
main.py: fájl
notes.txt: fájl
requirements.txt: fájl

instance: mappa
database.db: fájl

website: mappa
__init__.py: fájl
auth.py: fájl
models.py: fájl
views.py: fájl

templates: mappa

A website mappa tartalmazza az alkalmazás forráskódját. Az __init__.py fájl az alkalmazás belépési pontja. Az auth.py fájl tartalmazza az autentikációs rendszert. Az models.py fájl tartalmazza az adatbázis modelljeit. Az views.py fájl tartalmazza a nézeteket, amelyek megjelenítik az adatokat a felhasználó számára. A templates mappa tartalmazza az HTML sablonokat, amelyeket a nézetek használnak.

Az `AP_PRTFLMNGR` mappa tartalmazza a következő fájlokat:

- `Icon?`: ikon fájl
- `README.md`: leírás a projekt használatáról
- `VSCODE.md`: leírás a Visual Studio Code használatáról
- `main.py`: fő alkalmazás fájl
- `notes.txt`: jegyzetek
- `requirements.txt`: Python csomagok listája

A `./__pycache__` mappa tartalmazza a `yfinance.cpython-39.pyc` fájlt.

Az `./instance/database.db` fájl az adatbázis fájlja.

Az alkalmazás forráskódja a *Model-View-Controller (MVC)* tervezési mintát követi. Az auth.py fájl tartalmazza az autentikációs rendszert, amely a Model réteghez tartozik. Az models.py fájl tartalmazza az adatbázis modelljeit, amelyek szintén a Model réteghez tartoznak. A views.py fájl tartalmazza a nézeteket, amelyek megjelenítik az adatokat a felhasználó számára. A templates mappa tartalmazza az HTML sablonokat, amelyeket a nézetek használnak.

Melyik fájl - melyik réteghez tartozik az MVC pattern-ben:

*Model réteg:*
auth.py: autentikációs rendszer
models.py: adatbázis modelljei

*View réteg:*
views.py: nézetek, amelyek megjelenítik az adatokat a felhasználó számára
templates: HTML sablonok, amelyeket a nézetek használnak

*Controller réteg:*
Az alkalmazás belépési pontja a website/__init__.py fájlban található.

A Controller réteg az alkalmazás belépési pontja. Az `__init__.py` fájlban található. Ez a fájl tartalmazza az alkalmazás konfigurációját és inicializálja az alkalmazást. Az alkalmazás inicializálása során beállítja az adatbázis kapcsolatot, a nézeteket és az autentikációs rendszert.

