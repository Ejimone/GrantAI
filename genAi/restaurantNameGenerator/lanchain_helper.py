import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0.7)

def generate_restaurant_name(cuisine):   
    prompt_template_name = PromptTemplate(
        input_variables=["Cuisine"],
        template="I want to open a restaurant for {Cuisine} food, suggest a fancy name for this"
    )
    prompt_template_items = PromptTemplate(
        input_variables=["Cuisine"],
        template="Suggest some menu items for {Cuisine} food, return it as a comma separated list"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="food_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["Cuisine"],
        output_variables=["restaurant_name", "food_items"]
    )

    response = chain({"Cuisine": cuisine})
    return response

# function to get the hisory
# def get_history():
#     return llm.get_history()


if __name__ == "__main__":
    print(generate_restaurant_name("Italian"))