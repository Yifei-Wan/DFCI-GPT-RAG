# RAG-GPT chatbot 🔌

This project facilitates the embedding of CSV and TXT files into a vector database using Azure OpenAI. It leverages Chroma DB to store these embeddings and provides an API interface for generating answers based on the vector database. This setup allows for advanced Retrieval-Augmented Generation (RAG) capabilities.
Currently, the demo is focused on OncDRS documents, showcasing how the system can be applied to real-world use cases in data retrieval and analysis.

## ⚙️  Prerequisites

[Poetry](https://python-poetry.org) is a tool for dependency management and packaging in Python.

If you are already familiar with Poetry, or are comfortable setting up your own environment with other tools, you can probably skip this.

### Installing Poetry & Azure CLI

#### For macOS this would be the suggested way:

- Install brew: 

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install poetry using: 
```
brew install poetry
```

- Install Azure CLI
```
brew install azure-cli
```

### Installing GPT4DFCI API dependencies

After installing Poetry, navigate to the directory you are interested in and run:

```
poetry install --no-root
```

This should create a virtual environment with the dependencies specified in `pyproject.toml` installed.

### Set up vector database & login Azure
Download the vector database based on [OncDRS documents](https://wiki.dfci.harvard.edu:8443/oncdoc) from the S3 bucket, and log in to Azure:
```
bash chatbot_setup.sh
```

Close the window after logging in and get back to the shell.

## 🟢  Run the chatbot demos

### Set up environment variables
Please copy the template file `env_template` to create `.env` and fill in the following values:

```
AZURE_OPENAI_ENDPOINT=https://...
AZURE_OPENAI_ENTRA_SCOPE=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
CHROMADB_STORAGE_PATH=./chromadb
```

`AZURE_OPENAI_ENDPOINT` should be the GPT4DFCI API endpoint, without the `/openai` suffix.

`AZURE_OPENAI_ENTRA_SCOPE` should be the scope required for the bearer token, the UUID `client_id`.

`CHROMADB_STORAGE_PATH` should be the path to the ChromaDB vector database.


### VPN

```
Turn on the VPN or make sure you are running from an on-prem resource.
```

### Run the Semantic chatbot demo
```
bash chatbot_demo.sh -q "<Your question about OncDRS>"
```

### Run the Text-to-SQL chatbot demo
One test SQLite database `example.db` has been established in `tests` folder based on CSV file: `tests/2023-12-11_1_05pm.csv`.
```
python sql_query_agent.py -q "<Your question about test data in example.db>"
```

### Update the vector database to date
To update the local vector database with the latest data, simply rerun the setup process:
```
bash chatbot_setup.sh
```


### Shutting down

When finished working, shut the current virtual environment with

```
deactivate
```

# 🎫 License

The GNU GPL v3 version of GPT4DFCI is made available via Open Source licensing. The user is free to use, modify, and distribute under the terms of the GNU General Public License version 3.

Commercial license options are available also, and include additional features.


# 📧 Contact

Questions? Comments? Suggestions? Get in touch!

yifei_wan@dfci.harvard.edu
