from dataiku.llm.python import BaseLLM
from dataiku.langchain.dku_llm import DKUChatLLM
import dataiku

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


system_prompt = """You are a SQL generator for Paxlovid analytics.
Given a natural language question about Paxlovid (e.g., net sales, gross sales, date ranges),
RETURN ONLY a SQL query (no commentary). The text output of your response will be executed exactly as it is on the table paxlovid_sales with columns such as date, region, gross_sales, net_sales. Infer simple filters from the text."""
