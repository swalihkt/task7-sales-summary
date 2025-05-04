Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>>
>>> # Connect and create the database
>>> conn = sqlite3.connect("sales_data.db")
>>> cursor = conn.cursor()
>>>
>>> # Create a sales table
>>> cursor.execute('''
...     CREATE TABLE sales (
...             id INTEGER PRIMARY KEY,
...                     product TEXT,
...                             quantity INTEGER,
...                                     price REAL
...                                         )
...                                         ''')
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    cursor.execute('''
    ~~~~~~~~~~~~~~^^^^
        CREATE TABLE sales (
        ^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
                                            )
                                            ^
                                            ''')
                                            ^^^^
sqlite3.OperationalError: table sales already exists
>>>
>>> import os
>>> import sqlite3
>>> import os
>>> import sqlite3
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> conn = sqlite3.connect("sales_data.db")
>>> cursor = conn.cursor()
>>>
>>> cursor.execute('''
...     CREATE TABLE sales (
...             id INTEGER PRIMARY KEY,
...                     product TEXT,
...                             quantity INTEGER,
...                                     price REAL
...                                         )
...                                         ''')
<sqlite3.Cursor object at 0x0000020DA3697B40>
>>>
>>> sample_data = [
...     ('Apples', 10, 1.5),
...         ('Bananas', 5, 0.8),
...             ('Oranges', 8, 1.2),
...                 ('Apples', 7, 1.5),
...                     ('Bananas', 10, 0.8),
...                         ('Oranges', 3, 1.2),
...                         ]
>>>
>>> cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
<sqlite3.Cursor object at 0x0000020DA3697B40>
>>> conn.commit()
>>> print(" New sample data inserted.")
 New sample data inserted.
>>> query = """
... SELECT
...     product,
...         SUM(quantity) AS total_qty,
...             SUM(quantity * price) AS revenue
...             FROM sales
...             GROUP BY product
...             """
>>>
>>> df = pd.read_sql_query(query, conn)
>>> conn.close()
>>> print("\n Sales Summary:")

 Sales Summary:
>>> print(df)
   product  total_qty  revenue
0   Apples         17     25.5
1  Bananas         15     12.0
2  Oranges         11     13.2
>>>
>>> df.plot(kind='bar', x='product', y='revenue', legend=False)
<Axes: xlabel='product'>
>>> plt.title("Revenue by Product")
Text(0.5, 1.0, 'Revenue by Product')
>>> plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')
>>> plt.tight_layout()
>>> plt.savefig("sales_chart.png")
>>> plt.show()
