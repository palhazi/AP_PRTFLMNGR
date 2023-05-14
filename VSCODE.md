**Fájlok összehasonlítása VSCODE-ban**

A Visual Studio Code (VS Code) beépített támogatást nyújt fájlok összehasonlítására a "Diff Editor" segítségével. A Diff Editor lehetővé teszi, hogy két fájl különbségeit egymás mellett jelenítse meg, és megmutassa a hozzáadott, eltávolított vagy módosított sorokat. A fájlok összehasonlításához a VS Code-ban kövesd az alábbi lépéseket:

1. Nyisd meg a két fájlt, amelyet össze szeretnél hasonlítani a VS Code-ban.
2. Kattints a "File Explorer" (Fájlkezelő) ikonra a VS Code bal oldali oldalsávján.
3. Tartsd lenyomva a `Ctrl` (Windows/Linux) vagy a `Cmd` (macOS) billentyűt, és válaszd ki a két fájlt a fájlkezelőben.
4. Jobb egérgombbal kattints a kijelölt fájlokra, és válaszd az "Compare Selected" (Kijelöltek összehasonlítása) lehetőséget a helyi menüből.

A Diff Editor megnyílik, és megjeleníti a két fájl közötti különbségeket.

Emellett a VS Code beépített Git támogatása is lehetővé teszi a változtatások összehasonlítását a verziókezelőben. Ha a munkaterület egy Git repository, akkor a "Source Control" (Forráskódkezelő) panelen belül megtekintheted a módosításokat és összehasonlíthatod a jelenlegi állapotot a korábbi commitokkal.

Ha további funkciókat szeretnél a fájlok összehasonlításához, számos bővítmény érhető el a VS Code piacterén, például a "Compare Folders" vagy a "Partial Diff", amelyek további összehasonlítási lehetőségeket kínálnak.


*Verzió kezelő*

A Visual Studio Code (VS Code) egy nagyon népszerű közvetlenül integrálva van a Git verziókövető rendszerrel. Ezen keresztül könnyen lehet használni a Git funkciókat, mint például a commit, push és a szinkronizálás. Az említett parancsok a következőket jelentik:

1. **Commit**: A Git rendszerben a commit parancs lényegében egy "pillanatkép" készítése a kódbázisról. Ez azt jelenti, hogy elmenti a fájlok jelenlegi állapotát, és lehetővé teszi, hogy a későbbiekben visszatérhess a commit által rögzített állapotra. A commit parancs használatakor általában meg kell adni egy üzenetet is, amely leírja, hogy mi változott a commit által.

2. **Commit and Push**: Ez a parancs két műveletet hajt végre egyszerre. Először elmenti a változásokat egy új commitban (ahogy azt az előbb leírtam), majd a push parancs segítségével elküldi ezeket a változásokat a távoli repozitóriumba (általában egy GitHub vagy GitLab szerveren van). Ezáltal a többi fejlesztő is láthatja és letöltheti a változásokat.

3. **Commit and Sync**: Ez a parancs hasonló a "Commit and Push"-hoz, de egy extra lépéssel kiegészülve. A "Commit and Sync" parancs használatakor a VS Code először elmenti a változásokat egy commitban, majd szinkronizálja a helyi repozitóriumot a távoli repozitóriummal. Ez azt jelenti, hogy nem csak elküldi a saját változásokat a távoli repozitóriumhoz (push), hanem le is tölti a távoli repozitóriumban történt összes új változást (pull). Ez a parancs hasznos lehet, ha egyszerre szeretnénk frissíteni a saját kódunkat és letölteni a többi fejlesztő által végzett módosításokat.

**1 Fájl commitolása**

Az egyes fájlok külön-külön commitolásához a Visual Studio Code-ban a következő lépéseket követheted:

1. Nyisd meg a Source Control nézetet. A bal oldali oldalsávon kattints a Git ikonra (három ágazatot ábrázoló ikon).

2. Ebben a nézetben megjelennek azok a fájlok, amelyeken változás történt. 

3. Egyesével commitolhatod a fájlokat a következőképpen:
   - Keresd meg azt a fájlt, amit commitolni szeretnél.
   - Kattints a fájl nevének jobb oldalán található "+" ikonra. Ezzel a művelettel a fájl hozzáadásra kerül a "staging area"-hoz -- módosítások előjegyzésre kerülnek, amit Git szóhasználattal "stage"-elésnek hívunk. Ez azt jelenti, hogy a fájl készen áll a commitolásra.
   
4. Írd be a commit üzenetet a felső mezőbe.

5. Kattints a "Commit" gombra, ami a commit üzenet beviteli mezője felett van, és egy pipát ábrázol.

Ha csak ezt az egy fájlt adtad hozzá a "staging area"-hoz, akkor csak ennek a változásai kerülnek commitolásra. Ha több fájl is volt a listában, de csak ezt az egyet adtad hozzá, akkor a többi fájl változásai nem kerülnek bele ebbe a commitba. 

A pusholáshoz kattints a bal oldali oldalsávon lévő felhő ikonra vagy használd a "Git: Push" parancsot a Command Palette-ben (`Ctrl+Shift+P` vagy `Cmd+Shift+P` Mac-en). Ez a parancs feltölti a legutóbbi commitokat a távoli repozitóriumba.

*Mergelés Githubon!*

Általában a "master" ág a fő fejlesztési ág, amely a projekt stabil verzióját tartalmazza. A "dev" vagy "development" ág általában egy olyan ág, ahol a fejlesztés folyik, és amikor a fejlesztés befejeződött és stabil, a változásokat összevonják a "master" ágba.

A "Pull Request" a GitHub sajátossága, és lehetővé teszi a fejlesztők számára, hogy bejelentsék, hogy szeretnék összevonni munkájukat egy másik ágba. Ezáltal a csapat többi tagja áttekintheti a módosításokat, hozzászólhat, tesztelhet és elfogadhatja (vagy elutasíthatja) az összevonást.

A "védett ág" olyan ág, amelyre vonatkozóan további korlátozások vannak beállítva. Például megakadályozhatja a véletlen törlést, a nem ellenőrzött commitokat vagy a változások közvetlen pusholását. Ez általában a "master" ág, mivel ez a projekt stabil verzióját tartalmazza, és a véletlen hibákat minimálisra szeretnénk csökkenteni.

*A GitHubon a két ág összehasonlításához kövesse az alábbi lépéseket:*

1. Menjen a projekt GitHub oldalára.
2. Kattintson az ágak lenyíló menüjére (általában a "master" vagy "main" ágat mutatja alapértelmezetten).

3. A lenyíló menüben kiválasztja azt az ágat, amelyet össze szeretne hasonlítani egy másikkal.
   
4. Ezután kattintson a "Compare" vagy "Összehasonlítás" gombra.

5. A következő oldalon két lenyíló menüt láthat: az egyik a "base" (alap) ágat jelöli, a másik pedig a "compare" (összehasonlítás) ágat. A "base" ág az az ág, amelyhez képest összehasonlítást végez, míg a "compare" ág az az ág, amelynek változásait összehasonlítja.
   
6. Ha beállította az ágakat, az oldal megmutatja az összehasonlítást: a zöld színű sorok azok, amelyek hozzá lettek adva, a piros színű sorok pedig azok, amelyek törölve lettek az adott ágban a "base" ághoz képest.

Ez az összehasonlítás lehetővé teszi, hogy lássa a két ág közötti különbségeket, és szükség esetén "Pull Request"-et hozzon létre az összevonásra. Ez különösen hasznos, ha több fejlesztő dolgozik a projekten, és össze szeretnék vonni munkájukat.