from db.connection import get_connection

TEST_QUERY = """
SELECT
    *
FROM
    Employees
ORDER BY
    EmployeeID ASC
LIMIT 
    5
;
"""

TEST_QUERY_2 = """
DESC Employees;
"""

def fetch_all(query: str):
    """クエリを渡して全件取得する
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            # カラム名のリストを取得
            columns = [col[0] for col in cur.description]
            # レコードセットを取得（`pydoc.Row`オブジェクトのリスト）
            rows = cur.fetchall()
            # カラム名のリストと`Row`オブジェクトのリストを返却
            return columns, rows

def describe_table(table_name: str):
    """`DESC`コマンドを使ってテーブル構造を取得
    """
    query = f"DESC {table_name};"
    return fetch_all(query)
