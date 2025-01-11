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
# tools = load_tools(["wikipedia", "llm-math"], llm=llm)
tools = load_tools(["serpapi","llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
llm = OpenAI(temperature=0.7)
memory = ConversationBufferMemory()
chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory)
name = chain.run("Nigerian")
print(name)




# question = agent.run("Elon Musk network 2024")
# print(question)
print(chain.memory.buffer)
convo = ConversationChain(llm=OpenAI(temperature=0.7))
print(convo.prompt)
print(convo.prompt.template)

print(convo.run("What is the capital of Nigeria?"))
print(convo.memory)