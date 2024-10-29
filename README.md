![Architecture](https://github.com/FaisalxWattoo/SQL-to-Text-Using-Google-Gemini-Pro-API/blob/main/images/sqltotwxtstreamlitfrontend.png)

... 
# GEMINI APP TO RETRIEVE SQL DATA FROM SQLITE DATABASE
====================================================

## Overview
This project showcases a Streamlit web application designed to facilitate user interaction with a PostgreSQL database through a natural language interface. It leverages OpenAI's models for interpreting user queries and the sql.py script for executing SQL commands, streamlining data access without prior SQL knowledge.
## Setup Instructions
---------------

### Obtain an API Key
To interact with OpenAI's models, obtain an API key by registering with OpenAI. This key is essential for accessing the language model services.

### Configure Environment Variable
```plaintext
Create or update `.env` file in the root directory with:
OPENAI_API_KEY=<your-openai-api-key>
DATABASE_URL=<your-database-connection-string>
```

### Install Required Libraries
Ensure your environment is prepared by installing the necessary dependencies:
```bash
pip install -r requirements.txt
```

### Run the App
Activate the Streamlit application using:
```bash
streamlit run app.py
```

### app.py:
This file contains the Streamlit application logic. It handles the web interface, receives user inputs, and communicates with the OpenAI API to interpret natural language queries into SQL.

### sql.py:
A utility script that forms the bridge between the application and the PostgreSQL database. It executes SQL queries generated from user inputs and returns the results to the application for display.

By following these instructions, you can set up and run a web application that simplifies querying a PostgreSQL database using natural language processed by OpenAI's powerful AI models.
