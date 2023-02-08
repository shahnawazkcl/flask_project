from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views", static_folder='static')

# add home route
@views.route("/")
def home():
    return render_template("index.html", name="Ali", age=36, occupation='Researcher')

# add profile route
# use query parameter
@views.route("/profile/")
def profile():
    args = request.args
    name = args.get("name")
    return render_template("profile.html", name=name)

# add about route
@views.route("/about")
def about():
    return render_template("about.html")

# add json route an return in json format
@views.route("/json_example")
def get_json():
    atrribute_dict = {
        "user_id":"11001",
        "user_name":"Ali", 
        "user_age": "36",
        "user_ocuupation": "Researcher"
    }
    return jsonify(atrribute_dict)

#add another endpoint data to get the data and return jsonified
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# send data static data file
@views.route("/api/data")
def send_data():
    return views.send_static_file("data.json")

# redirect
@views.route("/goToHome")
def goToHome():
    return redirect(url_for("views.home"))
