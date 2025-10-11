from flask import Flask, render_template, abort, request
import pyodbc
import db.queries as db

app = Flask(__name__)

# クエリ実行失敗時返却用データ（笑）
FAILED_COLUMNS = ["( ´,_ゝ`)", "ち～ん（笑）"]
FAILED_ROWS = [
    ["残念ｗ", "レコードセットが返らなかったよｗｗｗ"]
]

DEFAULT_COLUMNS = ["( ´_ゝ`)", "クエリ未実行"]
DEFAULT_ROWS = [
    ["(･ω･)", "クエリを入力して実行ボタンをクリックしてね！"]
]

# トップページ
@app.route("/", methods=["GET", "POST"])
def index():
    # POSTリクエストのとき
    if request.method == "POST":
        # フォームからクエリを取得
        sql_query = request.form.get("sql_query", "").strip()
        # クエリ実行 -> レコードセット取得
        try:
            columns, rows = db.fetch_all(sql_query)
        except Exception as e:
            columns = FAILED_COLUMNS
            rows = FAILED_ROWS.copy()
            # エラー情報を追加
            rows.append(["原因はたぶん……", str(e)[:80] + "..."])
    # GETリクエストのとき
    else:
        sql_query = ""
        # デフォルトの擬似テーブルを表示
        columns, rows = [DEFAULT_COLUMNS, DEFAULT_ROWS]
    print(columns, rows)
    # レコードセットをテンプレートに渡す
    return render_template(
        "pages/index.html", 
        columns=columns, 
        rows=rows, 
        table_names=db.TABLE_NAMES, 
        sql_query=sql_query
    )

# 各テーブルの構造表示用ページ
@app.route("/table/<table_name>")
def show_table_structure(table_name):
    # 表示するテーブル名のリスト
    allowed_tables = db.TABLE_NAMES
    # テーブル名がリストになかったら404
    if table_name not in allowed_tables:
        abort(404)
    
    # DESC文実行
    fields, values = db.describe_table(table_name)

    # テンプレートにデータを投げる
    return render_template(
        "pages/table.html", 
        table_names=allowed_tables, 
        table_name=table_name, 
        columns=fields, 
        rows=values
    )

if __name__ == "__main__":
    app.run(debug=True)
