import os

from flask import Flask, redirect, send_file, make_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)

urls = {
    "github": "https://github.com/kitki30",
    "stick": "https://github.com/stickfirmware",
    "stickrepo": "https://github.com/stickfirmware/stick/",
    "devicetable": "https://github.com/stickfirmware/stick-tutorials/blob/main/install/table.md",
    "tutorials": "https://www.youtube.com/playlist?list=PLTu2NSjIK0c7TVbUVAlP5KkjpFISeaogt",
    "esptool": "https://espressif.github.io/esptool-js/",
    "mpydownloads": "https://micropython.org/download/",
    "thonnydownloads": "https://thonny.org/",
    "trello": "https://trello.com/b/ZT1qrlDO/stick-firmware",
    "docs": "https://docs.kitki30.tk",
    "myip": "https://api.kitki30.tk/ip",
    "converter": "https://convert.kitki30.tk/"
}

def redirect_404():
    # 404 page
    path = os.path.join(BASE_DIR, "pages", "err_invalid.html")
    if not os.path.isfile(path):
        return "404 Not Found", 404

    response = make_response(send_file(path))
    response.status_code = 404
    return response

@app.route('/<code>')
def short_redirect(code):
    target = urls.get(code)
    if target:
        return redirect(target)
    
    return redirect_404()

@app.route('/view/<code>')
def view_url(code):
    target = urls.get(code)
    if target:
        return target, 200
    
    return redirect_404()

@app.route('/')
def main():
    return redirect("https://www.kitki30.tk/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
