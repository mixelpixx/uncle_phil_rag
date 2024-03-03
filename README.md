# OpenAI Chatbot with ChromaDB

This project is a simple implementation of an OpenAI chatbot that uses ChromaDB for data storage and retrieval.

## Setup

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.

## Running on Windows 10
+
1. Make sure you have Python and pip installed on your machine. If not, you can download Python [here](https://www.python.org/downloads/) and pip will be installed with it.
2. Clone the repository by running `git clone <repository-url>`.
3. Navigate to the project directory and install the required dependencies by running `pip install -r requirements.txt`.
4. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key. You can do this by running `setx OPENAI_API_KEY "<your-api-key>"` in the command prompt.
5. Run the script `main.py` to start the Flask server by running `python main.py`.
6. Open another command prompt, navigate to the `GUI` directory and run the Flutter application by running `flutter run`.

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
