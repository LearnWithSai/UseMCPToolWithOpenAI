from mcp.server.fastmcp import FastMCP
import pyodbc
import pandas as pd

mcp = FastMCP("orders_server") 
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SAIKIRAN;"
    "DATABASE=funcdb;"
    "UID=sa;"
    "PWD=SAIkiran123;"
    "TrustServerCertificate=yes;"
    )

@mcp.tool()
def get_order_details(order_id):
    "get order details order_id;"

    df = pd.read_sql_query("select * from orders where OrderID = ?", conn, params=(order_id))
    return df.to_json(orient='records', indent=4)

@mcp.tool()
def delete_order(order_id):
    "delete order by order_id"
    cursor = conn.cursor()
    cursor.execute("delete from orders where OrderID = ?", (order_id,))
    conn.commit()
    if cursor.rowcount == 0:
        cursor.close()
        return {"found": False, "order_id": order_id}
    cursor.close()
    return {"found": True, "order_id": order_id}

@mcp.tool()
def get_all_orders():
    "get all orders"
    df = pd.read_sql_query("select * from orders", conn)
    return df.to_json(orient='records', indent=4)

@mcp.tool()
def get_order_by_customer_name(customer_name):
    "find order by customer name"
    df = pd.read_sql_query("select * from orders where OrderBy = ?", conn, params=(customer_name,))
    return df.to_json(orient='records', indent=4)

@mcp.tool()
def get_order_by_order_name(order_name):
    "find order by order name"
    df = pd.read_sql_query("select * from orders where OrderName = ?", conn, params=(order_name,))
    return df.to_json(orient='records', indent=4)

if __name__ == "__main__":
    mcp.run()
    