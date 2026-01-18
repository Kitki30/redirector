import os
import config

from flask import Flask, redirect, send_file, make_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)

def redirect_404():
    # 404 page
    path = os.path.join(BASE_DIR, config.pages_directory, config.404_page)
    if not os.path.isfile(path) or not config.allow_404:
        return "404 Not Found", 404

    response = make_response(send_file(path))
    response.status_code = 404
    return response

# Redirect to the destination
@app.route('/<code>')
def short_redirect(code):
    target = config.urls.get(code)
    if target:
        return redirect(target)

    return redirect_404()

# Show code destination
@app.route('/view/<code>')
def view_url(code):
    target = config.urls.get(code)
    if target:
        return target, 200

    return redirect_404()

# Main page redirect
@app.route('/')
def main():
    return redirect(config.main_page)

if __name__ == '__main__':
    app.run(host=config.host_ip, port=config.host_port)
