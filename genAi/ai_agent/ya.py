import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory #this is used to get the memory of the conversation, the second helps in reducing the question to the last n number of questions, thereby reducing the token length
from langchain import OpenAI
from langchain.chains import LLMChain, ConversationChain
llm = OpenAI(temperature=0.7)
from dotenv import load_dotenv
load_dotenv()
prompt_template_name = PromptTemplate(
    input_variables = ["cuisine"],
    template = "I want to open a restaurant for {cuisine}, suggest me some names for it."
)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
memory = ConversationBufferWindowMemory(k=1)
convo = ConversationChain(llm=OpenAI(temperature=0.7), memory=memory)
print(convo.run("How long does it take to travel from Delhi to Bangalore?"))
print(convo.run("what is 2+2?\n"))