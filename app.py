from flask import Flask
from views.prompt_view import prompt_bp

app = Flask(__name__)
app.register_blueprint(prompt_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
