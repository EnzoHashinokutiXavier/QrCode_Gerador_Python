from flask import Flask, render_template, request
import qrcode 

app = Flask(__name__)

def gerarImagem(link):
    # Transforma o link em qrcode e armazena em "imagem"
    imagem = qrcode.make(link)
    # Salva imagem como arquivo png
    imagem.save("static/qr.png", "PNG")


# Pagina inicial
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/imagem", methods=["POST"])
def qrcode_view():
    link = request.form.get("link", "").strip()
    if not link:
        link = "https://www.youtube.com/watch?v=ivV-kssG3NI"
    gerarImagem(link)
    return render_template("qrcode.html")