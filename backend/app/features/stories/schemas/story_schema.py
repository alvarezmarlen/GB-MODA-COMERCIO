"""Marshmallow schemas for story request validation."""

from marshmallow import Schema, fields, validate, EXCLUDE


class StorySchema(Schema):
    """Schema for validating story creation requests (POST /stories)."""

    user_id = fields.Integer(required=True, strict=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=200))
    content = fields.String(required=True, validate=validate.Length(min=1))
    origin_country = fields.String(required=True, validate=validate.Length(min=1, max=100))
    profession = fields.String(required=True, validate=validate.Length(min=1, max=100))
    age_range = fields.String(required=True, validate=validate.Length(min=1, max=50))

    class Meta:
        unknown = EXCLUDE


class StoryUpdateSchema(Schema):
    """Schema for validating story update requests (PUT /stories/<id>)."""

    user_id = fields.Integer(strict=True)
    title = fields.String(validate=validate.Length(min=1, max=200))
    content = fields.String(validate=validate.Length(min=1))
    origin_country = fields.String(validate=validate.Length(min=1, max=100))
    profession = fields.String(validate=validate.Length(min=1, max=100))
    age_range = fields.String(validate=validate.Length(min=1, max=50))

    class Meta:
        unknown = EXCLUDE


class StoryFilterSchema(Schema):
    """Schema for validating story filter query params (GET /stories)."""

    user_id = fields.Integer()
    origin_country = fields.String(validate=validate.Length(min=1, max=100))
    profession = fields.String(validate=validate.Length(min=1, max=100))
    age_range = fields.String(validate=validate.Length(min=1, max=50))

    class Meta:
        unknown = EXCLUDE
