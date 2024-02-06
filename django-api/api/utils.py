from django.conf import settings
import constantsp

from langchain.llms import OpenAI
import cx_Oracle
import os
from dotenv import load_dotenv
import tiktoken
from langchain.chains import load_chain
from langchain.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine
import openai
import sqlite3
import pandas as pd
import glob
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType



import os
os.environ["OPENAI_API_KEY"] = constantsp.APIKEY


def create_sqlite_db(csv_files, db_path, db_name):

    db_file_path = f"{db_path}/{db_name}"
    
    conn = sqlite3.connect(db_file_path)

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        table_name = csv_file.split('.')[0]

        df.to_sql(table_name, conn, index=False, if_exists='replace')

    conn.close()
csv_files = glob.glob('r/*.csv')
db_name = 'sample-or.db'
db_path = 'r/'
create_sqlite_db(csv_files, db_path, db_name)





def send_code_to_api(self):

    db = SQLDatabase.from_uri(f"sqlite:///./r/sample-or.db")


    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS
        
    )
    return agent_executor.run(self)