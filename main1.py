from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            })
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="POST'>
      <label value="0"> Rotate by: </label>
      <input type = "text" name = "rot"></input>

    </body>
</html>
"""


@app.route("/")

def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypt_text = rotate_string (encrypt_text
    return form.format(encrypt_text))

def index():
    return form.format("")
app.run 