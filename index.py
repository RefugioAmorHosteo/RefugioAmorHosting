from app import app

#IMPORT BLUE PRINTS
from routes.Tarot import Tarot, Terminosycondiciones

###### APP MAIN #######
app.register_blueprint(Tarot)
app.register_blueprint(Terminosycondiciones)


if __name__ == '__main__':
    app.run(debug=True)
