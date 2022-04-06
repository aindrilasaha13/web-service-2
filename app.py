import base64
from urllib import response
from flask import Flask, render_template, request
import requests ,io
import urllib.request
from PIL import Image

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.post("/calculate")
def calculate():
    value = request.form.get("N")
    image_url = "http://127.0.0.1:5001/"
    # image_url= "https://getimages-web-service.herokuapp.com/"
    response = requests.get(url = image_url, params={"N":value})
    img = response.content
    buffered = io.BytesIO(img)
    img_url = base64.b64encode(buffered.getvalue()).decode()
    return render_template("display.html",images={ 'image': img_url })

if __name__ == "__main__":
    app.run(debug=True,port=5002)