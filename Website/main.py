from flask import Blueprint, render_template, request, flash

main = Blueprint('main', __name__)

response = None

@main.route('/', methods = ["GET", "POST"])
def main1():
    global response
    if request.method == "POST":
        query = request.form.get("query")
        from .empathetic_response import empathic_message
        response = empathic_message(query)
    else:
        pass
    return render_template("submit.html", gpt_response = response)
