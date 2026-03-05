# AI SQL Data Analyst

An AI-powered data assistant that converts natural language questions into SQL queries, executes them on a database, visualizes the results, and generates human-readable insights.

This project demonstrates how Large Language Models (LLMs) can automate data analysis workflows by translating user questions into executable SQL queries and presenting the results through an interactive dashboard.

---

## Key Features

* Natural Language → SQL query generation
* Automated database querying
* Interactive data visualization
* AI-generated analytical insights
* Streamlit dashboard interface
* Lightweight SQLite database for testing

---

## System Architecture

```
User Question
      ↓
Streamlit Interface
      ↓
LLM (SQL Generator)
      ↓
Generated SQL Query
      ↓
SQLite Database
      ↓
Query Results
      ↓
Data Visualization
      ↓
AI Insight Summary
```

---

## Example Workflow

1. The user asks a question in natural language
2. The LLM converts the question into a SQL query
3. The query is executed against the database
4. The results are returned as a table
5. A visualization is automatically generated
6. The AI produces a short analytical insight

Example question:

```
Which hospital treated the most patients?
```

Generated SQL:

```sql
SELECT hospital, COUNT(*) as total_patients
FROM encounters
GROUP BY hospital
ORDER BY total_patients DESC;
```

---

## Project Structure

```
ai-sql-analyst
│
├── app.py                # Streamlit dashboard
├── query_engine.py       # Natural language to SQL engine
├── database_setup.py     # Database and sample data creation
│
├── requirements.txt
└── README.md
```

---

## Technology Stack

Python
Streamlit
SQLite
Pandas
Plotly
LangChain
OpenAI GPT Models

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-sql-analyst.git
```

Navigate to the project:

```
cd ai-sql-analyst
```

Create environment:

```
conda create -n sql-ai python=3.10
conda activate sql-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Setup the Database

Run the database initialization script:

```
python database_setup.py
```

This will create the local SQLite database used by the application.

---

## Run the Application

Start the Streamlit dashboard:

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## Example Questions to Try

* Which hospital treated the most patients?
* What department had the highest number of encounters?
* What is the average billing amount?
* What is the total billing amount by hospital?

---

## Example Output

The dashboard displays:

1. Generated SQL query
2. Query result table
3. Visualization chart
4. AI-generated analytical insight

Example insight:

> Mercy Hospital handled the highest number of patient encounters, indicating a larger patient demand compared to other facilities.

---

## Key Concepts Demonstrated

Natural Language to SQL systems
AI-powered data assistants
Database query automation
Data visualization pipelines
LLM-driven analytics

---

## Future Improvements

Multi-database support (PostgreSQL, BigQuery, Snowflake)
Automatic schema discovery
SQL query validation layer
Advanced visualization recommendations
Conversational memory for follow-up questions

---

## Author

Vijay Vempati
Healthcare Data Engineer building AI-powered data systems
