# Importáljuk a create_app függvényt a website modulból.
from website import create_app

# Létrehozzuk az app példányt a create_app függvény segítségével.
app = create_app()

# Ha a script közvetlenül futtatva van (nem importálva),
# akkor indítsuk el az alkalmazást.
if __name__ == '__main__':
    # Az alkalmazás futtatása a Flask fejlesztői kiszolgálóján,
    # a hibakeresési mód bekapcsolásával (debug=True).
    app.run(debug=True)

