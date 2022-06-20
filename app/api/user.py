from functools import partial
from flask import Response, current_app as app, request

from app.serializers import UserSchema, ProfessionalSchema

def signup_user():
    """
    path: /user/new
    method: Post
    Contract: {
        "name": "Afonso Medeiros",
            "email": "afonso@afonso.com",
            "password": "123456"
    }
    Response: {
        "created_at": "",
            "email": "",
            "id": 0,
            "name": "",
            "password": "",
            "updated_at": null
    }
    """
    us = UserSchema()
    user = us.load(request.json, partial=True)

    user.gen_hash()

    app.db.session.add(user)
    app.db.session.commit()
    Response.content_type = "Application/json"
    return us.jsonify(user), 200


def signup_professional():
    """
    path: /professional/new
    method: Post
    Contract: {
        "name": "Afonso Médico",
            "email": "afonso@afonso.com",
            "password": "123456"
    }
    Response: {
        "created_at": "",
            "email": "",
            "id": 0,
            "name": "",
            "password": "",
            "updated_at": null
    }
    """
    ps = ProfessionalSchema()
    professional = ps.load(request.json, partial=True)

    professional.gen_hash()

    app.db.session.add(professional)
    app.db.session.commit()
    Response.content_type = "Application/json"
    return ps.jsonify(professional), 200