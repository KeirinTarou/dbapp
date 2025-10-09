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
