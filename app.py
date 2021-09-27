from flask import Flask,render_template,request
from keras.models import load_model



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('trans.html')


@app.route('/haiku', methods=["GET", "POST"])
def haiku():
    if request.method == "POST":

        haikus = print_text().decode("utf-8")

        input_text = request.form["eng"]
        output_text = request.form.get('other')
        trans = request.form['langg']

        if trans == 'spa':
            trans = 'to Spanish'

        if trans == 'fra':
            trans = 'to French'

        language = {
            'input': input_text,
            'output': output_text,
            'trans': trans
        }

        return render_template("index.html", lang=language, text=haikus)

if __name__ == "__main__":
    app.run(port=8000,debug=True)
