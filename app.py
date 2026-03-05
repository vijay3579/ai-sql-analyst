import streamlit as st
import pandas as pd
import plotly.express as px
from query_engine import ask_database, generate_sql
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="AI SQL Data Analyst", layout="wide")

st.title("AI SQl Data Analyst")

st.write("Ask the question about the hospital dataset")

question=st.text_input("Enter your question")

if question:

	with st.spinner("Generating sql and running query...."):

		sql_query=generate_sql(question)

		df= ask_database(question)

	st.subheader("Generated SQL")

	st.code(sql_query, language="sql")

	st.subheader("Query Results")

	st.dataframe(df)

	if len(df.columns) >= 2:


		try:
			fig=px.bar(df,x=df.columns[0],y=df.columns[1])
			st.subheader("Visualization")
			st.plotly_chart(fig, use_container_width=True)
		except:
			pass


	llm = ChatOpenAI(model="gpt-4o-mini")

	insight_prompt= f"""

	You are data Analyst
	
	Based on the data below, provide a short insight.

	Data:
	{df}

	Insight:
	"""

	response = llm.invoke(insight_prompt)

	st.subheader(" AI Insight")

	st.write(response.content)

