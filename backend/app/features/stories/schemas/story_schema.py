"""Marshmallow schemas for story request validation."""

from marshmallow import Schema, fields, validate, EXCLUDE


class StorySchema(Schema):
    """Schema for validating story creation requests (POST /stories)."""

    user_id = fields.Integer(required=True, strict=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=200))
    content = fields.String(required=True, validate=validate.Length(min=1))
    origin_country = fields.String(required=True, validate=validate.Length(min=1, max=100))
    profession = fields.String(required=True, validate=validate.Length(min=1, max=100))
    age = fields.Integer(required=True, validate=validate.Range(min=0, max=150), strict=True)

    class Meta:
        unknown = EXCLUDE


class StoryUpdateSchema(Schema):
    """Schema for validating story update requests (PUT /stories/<id>)."""

    user_id = fields.Integer(strict=True)
    title = fields.String(validate=validate.Length(min=1, max=200))
    content = fields.String(validate=validate.Length(min=1))
    origin_country = fields.String(validate=validate.Length(min=1, max=100))
    profession = fields.String(validate=validate.Length(min=1, max=100))
    age = fields.Integer(validate=validate.Range(min=0, max=150), strict=True)

    class Meta:
        unknown = EXCLUDE


class StoryFilterSchema(Schema):
    """Schema for validating story filter query params (GET /stories)."""

    origin_country = fields.String(validate=validate.Length(min=1, max=100))
    profession = fields.String(validate=validate.Length(min=1, max=100))
    age = fields.Integer()

    class Meta:
        unknown = EXCLUDE
