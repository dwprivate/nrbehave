import sys

import behave

if __name__ == "__main__":
    print("NRBeHappy !")
    print(f"Version de python: {sys.version}")
    if not "3.11." in sys.version:
        print("La version python recommandée est 3.11. Vous voilà prévenus !")
    print(f"Version de behave: {behave.version.VERSION}")
