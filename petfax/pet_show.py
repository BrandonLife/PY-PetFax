from flask import Blueprint, render_template
import json

bp = Blueprint("pet_show", __name__, url_prefix="/pets")

pets = json.load(open("pets.json"))


@bp.route("/<pet_id>")
def pet_show(pet_id):
    id = int(pet_id)
    print(pets[id], "this is pets id page")
    return render_template("pet_show.html", pets=pets[id])
