import sqlite3
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

DB_PATH = "hospital.db"

def get_schema():

	schema="""

	Tables:

	patients(patient_id, name, age, gender)

    encounters(encounter_id, patient_id, hospital, department, admission_date)

    billing(bill_id, encounter_id, amount)
	"""

	return schema

def generate_sql(question):
	schema=get_schema()
	prompt = f"""

	You are a SQL expert.

	Return ONLY a valid SQLite SQL query.

	Do not include explanations.
	Do not include markdown.
	Do not include ```sql.

	Database schema:

	{schema}

	convert the following question into SQL.

	Question:
	{question}

	sql query:
	"""
	llm= ChatOpenAI(model="gpt-4o-mini")
	response = llm.invoke(prompt)

	sql_query = response.content.strip()
	#remove markdown formatting

	sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

	if ";" in sql_query:
		sql_query= sql_query.split(";")[0]+";"

	return sql_query


def execute_sql(query):


	conn=sqlite3.connect(DB_PATH)

	df=pd.read_sql(query,conn)

	conn.close()

	return df

def ask_database(question):

	sql_query=generate_sql(question)

	print("\n Generated SQL:\n", sql_query)

	results= execute_sql(sql_query)

	return results

if __name__ =="__main__":

	question=input("Ask the question about the hospital data:")

	df=ask_database(question)

	print("\n results:\n")

	print(df)

