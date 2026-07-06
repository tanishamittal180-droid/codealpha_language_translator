from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///translator.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

languages = {
    "Auto":"auto",
    "English":"en",
    "Hindi":"hi",
    "Punjabi":"pa",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Japanese":"ja",
    "Chinese":"zh-cn",
    "Urdu":"ur"
}


class History(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(500))
    translated = db.Column(db.String(500))
    source = db.Column(db.String(50))
    target = db.Column(db.String(50))
    time = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route("/")
def home():

    return render_template(
        "index.html",
        languages=languages
    )


@app.route("/translate", methods=["POST"])
def translate():

    try:

        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        if source=="auto":
            source=detect(text)

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        save=History(
            original=text,
            translated=translated,
            source=source,
            target=target,
            time=str(datetime.now())
        )

        db.session.add(save)
        db.session.commit()

        return jsonify({
            "translated":translated,
            "detected":source
        })

    except Exception as e:

        return jsonify({
            "translated":"Error: "+str(e)
        })


@app.route("/history")
def history():

    rows=History.query.all()

    data=[]

    for row in rows:

        data.append({
            "original":row.original,
            "translated":row.translated,
            "time":row.time
        })

    return jsonify(data)


@app.route("/speak",methods=["POST"])
def speak():

    text=request.form["text"]

    tts=gTTS(text=text)

    filename="static/output.mp3"

    tts.save(filename)

    return jsonify({
        "audio":filename
    })


if __name__=="__main__":
    app.run(debug=True)