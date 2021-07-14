"""main.py runs the main application.
"""

from engine import Log, Engine, GameManager


if __name__ == "__main__":
    eng = Engine("main", 800, 400, GameManager("gm"))
    Log.Main().Engine(eng.name).call()
