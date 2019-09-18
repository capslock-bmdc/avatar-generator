from PIL import Image
import io
from flask import Flask, Response
from flask_cors import CORS
from werkzeug.wsgi import FileWrapper

from generator import generate

app = Flask(__name__)
CORS(app)

@app.route('/')
def get():
    img_io = io.BytesIO()
    avatar = generate()
    avatar.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    #return send_file(img_io, mimetype='image/png')
    file_wrapper = FileWrapper(img_io)
    return Response(file_wrapper, mimetype="text/plain", direct_passthrough=True)

if __name__ == "__main__":
    app.run()