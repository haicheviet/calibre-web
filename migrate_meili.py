import sqlite3
import meilisearch
import os


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect(os.environ["LIB_PATH"])
conn.row_factory = dict_factory
cur = conn.cursor()



client = meilisearch.Client(os.environ["MEILI_HOST"], api_key=os.environ["MEILI_KEY"])
index = client.index('books')
index.update_settings({
  'searchableAttributes': [
      'title',
      'author_sort'
]})

df = cur.execute("select * from books;").fetchall()
print(df[0])
print(len(df))

index.add_documents(df)