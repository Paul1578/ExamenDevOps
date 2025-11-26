from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify(message="Hello, World, esto es para el examen de DevOps!")

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app


if __name__ == "__main__":
    app = create_app()
    # Cambia el host/port si lo necesitas
    app.run(host="0.0.0.0", port=80, debug=True)
