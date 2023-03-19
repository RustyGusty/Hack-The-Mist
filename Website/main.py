from flask import Blueprint, render_template, request, flash

main = Blueprint('main', __name__)

response = None

@main.route('/', methods = ["GET", "POST"])
def main1():
    global response
    if request.method == "POST":
        response = request.form.get("query")
    else:
        pass
    return render_template("submit.html", gpt_response = response)
