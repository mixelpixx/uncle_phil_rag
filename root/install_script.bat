- pyinstaller --onefile main.py
+ pyinstaller --onefile --add-data "chroma_db;chroma_db" --add-data "docs;docs" main.py