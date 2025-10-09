from flask import Flask, render_template
import pyodbc
import db.queries as db

app = Flask(__name__)

@app.route("/")
def index():
    # DBに接続してレコードセットを取得
    columns, rows = db.fetch_all(db.TEST_QUERY)

    # レコードセットをテンプレートに渡す
    return render_template(
        "pages/index.html", 
        columns=columns, 
        rows=rows
    )

if __name__ == "__main__":
    app.run(debug=True)
