# from flask_wtf import FlaskForm
# from wtforms import FileField, validators, TextAreaField
# import re
#
#
# class UploadForm(FlaskForm):
#     image = FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
#     # description = TextAreaField(u'Image Description')
#
#     def validate_image(form, field):
#         if field.data:
#             field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
