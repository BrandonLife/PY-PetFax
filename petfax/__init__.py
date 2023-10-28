from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, PetFax"

    from . import pet

    app.register_blueprint(pet.bp)

    from . import create_facts

    app.register_blueprint(create_facts.bp)

    from . import pet_show

    app.register_blueprint(pet_show.bp)

    return app
