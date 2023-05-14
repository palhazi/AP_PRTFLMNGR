# Importáljuk a create_app függvényt a website modulból.
from website import create_app

# Létrehozzuk az app példányt a create_app függvény segítségével.
app = create_app()

if __name__ == '__main__':
    # Az alkalmazás futtatása,
    # a hibakeresési mód bekapcsolásával (debug=True).
    app.run(debug=True)

