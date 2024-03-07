- documents = SimpleDirectoryReader("./docs/").load_data()
+ documents = SimpleDirectoryReader(os.path.join(sys._MEIPASS, "docs")).load_data()

- db = chromadb.PersistentClient(path="./chroma_db")
+ db = chromadb.PersistentClient(path=os.path.join(sys._MEIPASS, "chroma_db"))

- def check_database_exists():
-    return os.path.exists("./chroma_db")
+ def check_database_exists():
+    return os.path.exists(os.path.join(sys._MEIPASS, "chroma_db"))

- def rebuild_database():
-    if os.path.exists("./chroma_db"):
-        shutil.rmtree("./chroma_db")
+ def rebuild_database():
+    if os.path.exists(os.path.join(sys._MEIPASS, "chroma_db")):
+        shutil.rmtree(os.path.join(sys._MEIPASS, "chroma_db"))