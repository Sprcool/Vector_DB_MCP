from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import json

# =========================================================
# LLM
# =========================================================

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are an enterprise SQL AI Tutor specialized in Azure Data Engineering.

Generate enterprise-grade SQL questions.
Evaluate SQL answers concisely.
Avoid repeated scenarios.
Focus on production-oriented SQL thinking.
"""

# =========================================================
# QUESTION CHAIN
# =========================================================

question_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", """
Generate ONE SQL question.

Topic:
{topic}

Difficulty:
{difficulty}

Runtime Memory:
{runtime_memory}

Requirements:
- Azure Data Engineering scenario
- Real-world use case
- Avoid repeated scenarios
- No answer
""")
])

question_chain = (
    question_prompt
    | llm
    | StrOutputParser()
)

# =========================================================
# EVALUATION CHAIN
# =========================================================

evaluation_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", """
Evaluate SQL answer.

Question:
{question}

User Answer:
{user_answer}

STRICT FORMAT:

Evaluation Result:
Mistake Summary:
Performance Score:
Optimization Score:
Production Readiness Score:
""")
])

evaluation_chain = (
    evaluation_prompt
    | llm
    | StrOutputParser()
)

# =========================================================
# GENERATE QUESTION
# =========================================================

runtime_memory = {
    "weak_areas": ["recursive_cte"],
    "recently_used_scenarios": ["employee_hierarchy"]
}

question = question_chain.invoke({
    "topic": "CTE",
    "difficulty": "Intermediate",
    "runtime_memory": json.dumps(runtime_memory)
})

print("\n=== GENERATED QUESTION ===\n")
print(question)

# =========================================================
# EVALUATE ANSWER
# =========================================================

evaluation = evaluation_chain.invoke({
    "question": question,
    "user_answer": """
    WITH cte AS (
        SELECT * FROM employees
    )
    SELECT * FROM cte
    """
})

print("\n=== EVALUATION ===\n")
print(evaluation)