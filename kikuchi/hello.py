# hello.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<!DOCTYPE html>\
        <html>\
            <head>\
                <title>__(:3」∠)__なにみてんだよ</title>\
            </head>\
            <body>\
                <p>__(:3」∠)__なにみてんだよ</p>\
            </body>\
        </html>"

if __name__=="__main__":
    app.run()