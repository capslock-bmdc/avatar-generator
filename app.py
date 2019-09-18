from PIL import Image
import io
from flask import Flask, send_file
from flask_cors import CORS

from generator import generate

app = Flask(__name__)
CORS(app)

@app.route('/')
def get():
    img_io = io.BytesIO()
    avatar = generate()
    avatar.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run()