# OpenAI Chatbot with ChromaDB

This project is a simple implementation of an OpenAI chatbot that uses ChromaDB for data storage and retrieval.

## Setup

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.

## Running the Application on Windows 10

1. Make sure you have Python 3.8 or later installed. If not, download and install it from [here](https://www.python.org/downloads/).
2. Install pip, which is the package installer for Python. You can check if pip is installed by typing `pip --version` in the command prompt. If it is not installed, download and install it from [here](https://pip.pypa.io/en/stable/installation/).
3. Clone the repository by typing `git clone https://github.com/your-repo-link` in the command prompt.
4. Navigate to the project directory using `cd path-to-your-directory`.
5. Install the required dependencies by typing `pip install -r requirements.txt` in the command prompt.
6. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key. You can do this by typing `setx OPENAI_API_KEY your-api-key` in the command prompt.
7. Run the application by typing `python main.py` in the command prompt.

## Running the Flutter GUI

1. Make sure you have Flutter and Dart installed on your machine. If not, you can download and install them from [here](https://flutter.dev/docs/get-started/install).
2. Navigate to the /lib/ directory using `cd /lib/`.
3. Run the Flutter GUI by typing `flutter run` in the command prompt.

## Usage

Run the script `main.py` to start the chatbot. You can interact with the bot by typing your messages into the console. To exit the chatbot, type 'exit'.

The chatbot uses OpenAI's GPT-3 model to generate responses. It also uses ChromaDB to store and retrieve data. The data is stored in a local database located in the `chroma_db` directory.

## Rebuilding the Database

If you need to rebuild the database, you can do so by calling the `rebuild_database` function in `main.py`. This will delete the existing database and recreate it from the documents in the `docs` directory.

## Error Handling

The script includes basic error handling. If an error occurs while calling the OpenAI API or querying the database, the script will print an error message and continue running.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.
