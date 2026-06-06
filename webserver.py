from flask import flask

app = Flask("forever-rp-webserver")
@app.route("/")
def home():
    return "Forever RP Bot is online & volledig operationeel!"


def run():
    app.run(host="0.0.0.0", port=8080)

    def keep_alive():
        t = threading.Thread(target=run)
        t.start()