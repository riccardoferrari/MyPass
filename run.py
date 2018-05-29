from flask import Flask
from MyPass import app

if __name__ == "__main__":
    app.run(port = 4000, debug = True)