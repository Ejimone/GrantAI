import os
from dotenv import load_dotenv

load_dotenv()
# creating a prompt template
from langchain.prompts import PromptTemplate
import openai
from langchain.chains import LLMChain, SimpleSequentialChain


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.6)
# name = llm("I want to ioen a restaurant for insian food, suggest a fancy name for this")

prompt_template_name =  PromptTemplate(
    input_variables = ["Cuisine"],
    template = "I want to ioen a restaurant for {Cuisine} food, suggest a fancy name for this"
)
prompt_template_items =  PromptTemplate(
    input_variables = ["Cuisine"],
    template = "Suggest some menu items for {Cuisine} food, return it as a comma seperated list"
)


prompt_name = prompt_template_name.format(Cuisine="Indian")
chain = LLMChain(llm=llm, prompt=prompt_template_name)
chains2 = SimpleSequentialChain(chains = [chain, prompt_template_items])

print(prompt_name)
chain.invoke( "American")
print(chain.run( "American"))
response = chains2.run("American")
print(response)
