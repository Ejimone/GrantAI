import os
from langchain.chains import SimpleSequentialChain, LLMChain, SequentialChain
from langchain.llms import OpenAI
from dotenv import load_dotenv


load_dotenv()
import os
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.7)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


prompt_template_items = PromptTemplate(
    input_variables = ["Cuisine"],
    template = "Suggest some menu items for {Cuisine} food, return it as a comma seperated list"
)

food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)


prompt_template_name = (
    PromptTemplate(
        input_variables = ["Cuisine"],
        template = "I want to ioen a restaurant for {Cuisine} food, suggest a fancy name for this"
    )
)

new_chain = LLMChain(llm=llm, prompt=prompt_template_name)
chain = SimpleSequentialChain(chains = [new_chain, food_items_chain])
response = chain.run("Mexican")
print(response)


name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="food_items")


chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ["Cuisine"],
    output_variables = ["restaurant_name", "food_items"]
)

print(chain({
    "Cuisine": "Arabic"
}))