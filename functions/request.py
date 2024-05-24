from flask import request


def requestJson(atributo):
    try:
        return request.json[atributo]
    except:
        try:
            return request.form[atributo]
        except:
            return None