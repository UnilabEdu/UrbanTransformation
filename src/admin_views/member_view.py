from flask_admin.form.upload import ImageUploadField
from src.admin_views.base import SecureModelView
from flask import current_app

class MemberView(SecureModelView):
    form_overrides = {
        "image": ImageUploadField
    }

    form_args = {
        "image": {
            "base_path": lambda: current_app.config["UPLOAD_PATH"],
            "relative_path": "images/"
        }
    }