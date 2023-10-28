from flask import Blueprint, render_template


bp = Blueprint("fact", __name__, url_prefix="/pets")


@bp.route("/facts/new")
def fact():
    return render_template("create_facts.html")
