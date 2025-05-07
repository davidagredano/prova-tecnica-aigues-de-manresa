from flask import Flask, render_template, jsonify
import mqtt_client

app = Flask(__name__)

mqtt_client.init()


@app.route("/api/mqtt")
def mqtt_data():
    return jsonify({"value": mqtt_client.get_last_message()})


@app.route("/")
def index():
    return render_template("index.html")
