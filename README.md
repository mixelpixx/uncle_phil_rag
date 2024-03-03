# OpenAI Chatbot with ChromaDB

This project is a simple implementation of an OpenAI chatbot that uses ChromaDB for data storage and retrieval.

## Setup

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.

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