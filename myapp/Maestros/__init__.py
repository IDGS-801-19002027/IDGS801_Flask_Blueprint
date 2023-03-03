from flask import Flask, render_template, jsonify
from flask import request
from flask import redirect
from flask import url_for

app= Flask(__name__)
app.config['DEBUG']=True

@app.route("/", methods=['GET'])
def home():
    return jsonify({'Datos':'Hola'})

if __name__ == 'main':
    app.run()