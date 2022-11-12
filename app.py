from flask import Flask, render_template, request
from PIL import Image
import pyocr

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return "ファイルが選択されていません"
    file = request.files["file"]
    img = Image.open(file)
    # img.save("/static/fig.png")
    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )

    return render_template("index.html", txt=txt)


tools = pyocr.get_available_tools()
tool = tools[0]


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
