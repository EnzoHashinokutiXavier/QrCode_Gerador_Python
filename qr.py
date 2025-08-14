import qrcode # Biblioteca que gera qrcode através de link

# Transforma o link em qrcode e armazena em "imagem"
imagem = qrcode.make("https://www.youtube.com/watch?v=uCrGFFDC9wU")

# Salva imagem como arquivo png
imagem.save("qr.png", "PNG")