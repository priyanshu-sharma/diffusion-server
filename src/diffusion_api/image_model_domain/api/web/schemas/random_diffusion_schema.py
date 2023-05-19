from marshmallow import fields, Schema

class RandomDiffusionSchema(Schema):        
    prompt_list = fields.List(fields.String(), required=True)
    image_list = fields.List(fields.String())