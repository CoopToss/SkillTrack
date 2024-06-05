from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path, mimetype='application/javascript')

app.secret_key = 'cooperwashere'

if __name__ == '__main__':
    app.run(debug=True)
