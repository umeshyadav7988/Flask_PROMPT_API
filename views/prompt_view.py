from flask import Blueprint, request, jsonify
from services.prompt_service import get_prompt
from werkzeug.exceptions import BadRequest

prompt_bp = Blueprint("prompt", __name__)

@prompt_bp.route("/get-prompt", methods=["POST"])
def match_prompt():
    try:
        data = request.get_json(force=True)

        # Validate all required fields
        required_fields = ["situation", "level", "file_type", "data"]
        missing = [field for field in required_fields if field not in data or not data[field]]

        if missing:
            raise BadRequest("Missing Data")

        situation = data["situation"]
        level = data["level"]
        file_type = data["file_type"]

        # Get the matching prompt
        prompt = get_prompt(situation, level, file_type)
        return jsonify({"prompt": prompt}), 200

    except BadRequest as e:
        # ✅ Return only the description (e.g. "Missing Data")
        return jsonify({"error": e.description}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500
