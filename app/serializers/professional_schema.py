from marshmallow import fields, post_load
from app.extensions.marshmallow import ma
from app.models import Professional


class ProfessionalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'profession', 'created_at', 'updated_at')

    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    profession = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return Professional(**data)