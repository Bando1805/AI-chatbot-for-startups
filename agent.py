from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools_creation import tools
from API_keys import OPENAI_API_KEY


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm=ChatOpenAI(temperature=0,openai_api_key=OPENAI_API_KEY,max_tokens= 500)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)






