from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/resume.html')
def resume():
	return render_template("resume.html")

if __name__ == "__main__":
	app.run(debug=True, port=5000)
