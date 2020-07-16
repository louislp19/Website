from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/touchdesigner")
def touchdesigner():
	return render_template("touchdesigner.html")

@app.route("/3D_render")
def Renders():
	return render_template("3D_Renders.html")

@app.route("/bio")
def bio():
	return render_template("Biographie.html")

@app.route("/contact")
def contact():
	return render_template("Contact.html")

@app.route("/alta-mira")
def satoumi():
	return render_template("Alta-Mira.html")

@app.route("/mecaniques-fluides")
def MecaniqueFluides():
	return render_template("Mecanique-fluides.html")

@app.route("/satoumi")
def AltaMira():
	return render_template("Satoumi.html")

@app.route("/mitose")
def mitose():
	return render_template("Mitose.html")

@app.route("/projet-do")
def projetDo():
	return render_template("Projet-do.html")

@app.route("/lost-screen-dream")
def lostScreenDream():
	return render_template("Lost-screen-dream.html")

@app.route("/horizon")
def horizon():
	return render_template("Horizon.html")

@app.route("/electronique")
def electronique():
	return render_template("Electronique.html")

@app.route("/perturbations")
def perturbations():
	return render_template("Perturbations.html")

def currentTime ():
	time = strftime("%H:%M:%S", gmtime())
	return time


if __name__== "__main__":
	app.run(debug = True)

