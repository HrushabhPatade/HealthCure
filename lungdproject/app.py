from flask import Flask, render_template, request, url_for
import pickle

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home2.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route("/find")
def find():
	r1 = request.args.get("r1")
	if r1 == "no":
		a = 1
	else:
		a = 2
	r2 = request.args.get("r2")
	if r2 == "no":
		b = 1
	else:
		b = 2
	r3 = request.args.get("r3")
	if r3 == "no":
		c = 1
	else:
		c = 2
	r4 = request.args.get("r4")
	if r4 == "no":
		d = 1
	else:
		d = 2
	r5 = request.args.get("r5")
	if r5 == "no":
		e = 1
	else:
		e = 2
	r6 = request.args.get("r6")
	if r6 == "no":
		z = 1
	else:
		z = 2
	r7 = request.args.get("r7")
	if r7 == "no":
		g = 1
	else:
		g = 2
	r8 = request.args.get("r8")
	if r8 == "no":
		h = 1
	else:
		h = 2
	r9 = request.args.get("r9")
	if r9 == "no":
		i = 1
	else:
		i = 2
	r10 = request.args.get("r10")
	if r10 == "no":
		j = 1
	else:
		j = 2
	with open("lungc.model", "rb") as f:
		model = pickle.load(f)
	data = [[a,b,c,d,e,z,g,h,i,j]]
	print(data)
	res = model.predict(data)
 
	res1 = res[0]
	if res1 == "YES":
		msg = "Lung Cancer is Detected"
	else:
		msg = "Lung Cancer is not Detected"
	
	return render_template("form.html", m=msg)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)	