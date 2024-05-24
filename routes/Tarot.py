from flask import Blueprint,render_template,redirect,url_for,jsonify, request
#from utils.db import db
from functions.request import requestJson
#from models.models import *

Tarot = Blueprint("Tarot",__name__)
Terminosycondiciones = Blueprint("Terminosycondiciones",__name__)

@Tarot.route("/")
def getHome():
    listas = [
        {
            "title": "AMARRES",
            "desc": "Nuestros Amarres de Amor reavivan la llama perdida y reconstruyen los lazos que los unieron. Deja atrás la tristeza, da el paso para recuperar el amor y la armonía que mereces.","image": "https://cdn-icons-png.flaticon.com/512/5498/5498761.png",
            "color": "#D9AA48"
        },
        {
            "title": "ENDULZAMIENTO",
            "desc": "Con nuestros Endulzamientos, suavizas tensiones, fomentas el amor y atraes a tu ser amado constantemente. Transforma tu relación en fuente de felicidad duradera.","image": "https://img.freepik.com/iconos-gratis/atrapasuenos_318-797911.jpg?w=2000",
            "color": "#D9CD48"

        },
        {
            "title": "RETORNO AMOROSO",
            "desc": "La separación duele. Estamos aquí para ayudarte a recuperar lo que fue tuyo, con el hechizo perfecto para la reconciliación. Supera la distancia, ten una segunda oportunidad para el amor, perdón y felicidad juntos. Actúa ya, reclama tu felicidad y restaura la merecida conexión.","image": "https://simbolosysignificados.es/wp-content/uploads/1632220006_928_Simbolos-de-la-magia-y-su-significado.png",
            "color": "#D9BC48"
        },
        {
            "title": "CASAMIENTO ESPIRITUAL",
            "desc": "El amor se fortalece en la unión profunda. Trasciende lo físico para ser almas gemelas. Da el paso hacia un compromiso más significativo. Fortalece y da nuevo significado a tu relación.","desc":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
            "image": "https://img.freepik.com/iconos-gratis/hamsa_318-760593.jpg",
            "color": "#D99748"


        }
    ]
    testimonios = [
        {
            "numero": "1 / 8",
            "url": "../static/src/testimonio-1.webp"
        },
        {
            "numero": "2 / 8",
            "url": "../static/src/testimonio-2.webp"
        },
        {
            "numero": "3 / 8",
            "url": "../static/src/testimonio-3.webp"
        },
        {
            "numero": "4 / 8",
            "url": "../static/src/testimonio-4.webp"
        },
        {
            "numero": "5 / 8",
            "url": "../static/src/testimonio-5.webp"
        },
        {
            "numero": "6 / 8",
            "url": "../static/src/testimonio-6.webp"
        },
        {
            "numero": "7 / 8",
            "url": "../static/src/testimonio-7.webp"
        },
        {
            "numero": "8 / 8",
            "url": "../static/src/testimonio-8.webp"
        }
    ]
    return render_template("/main.html", listas=listas, testimonios=testimonios)


@Terminosycondiciones.route("/terminos-y-condiciones")
def getTerminosycondiciones():
    return render_template("/tyc.html")