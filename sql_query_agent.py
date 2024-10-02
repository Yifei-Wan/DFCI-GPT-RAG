import argparse
from langchain.agents import AgentExecutor
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from src.azure_client import token_provider, endpoint, api_version, completion_model
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage

SQL_PREFIX = """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

To start you should ALWAYS look at the tables in the database to see what you can query.
Do NOT skip this step.
Then you should query the schema of the most relevant tables."""

def create_langchain_agent(db_path: str) -> AgentExecutor:
    """Create a LangChain SQL agent connected to the SQLite database."""
    # Create a connection to the SQLite database
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    llm = AzureChatOpenAI(
        api_version=api_version,
        deployment_name=completion_model,
        azure_ad_token_provider=token_provider,  # Your Azure token provider.
        azure_endpoint=endpoint,
        temperature=0  # Adjust the temperature if needed.
    )

    # Create an agent with the SQL database and the Azure OpenAI LLM
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
    return agent_executor

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Query an SQLite database using LangChain and Azure OpenAI.')
    parser.add_argument('-q', '--question', type=str, required=True, help='The question to ask the database')
    parser.add_argument('-d', '--database', type=str, default='example.db', help='Path to the SQLite database file')
    
    args = parser.parse_args()

    # Create LangChain agent connected to the SQLite DB
    agent_executor = create_langchain_agent(args.database)

    # Query the SQL database
    system_message = SystemMessage(content=SQL_PREFIX)
    messages = [
        system_message,
        {"role": "user", "content": args.question}
    ]
    
    # Execute the query using the agent
    response = agent_executor.invoke(messages, handle_parsing_errors=True)
    print(f"\n------------------------------------\nAnswer: {response['output']}\n")