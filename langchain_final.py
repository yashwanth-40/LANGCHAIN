from langchain.llms import OpenAI
import secret_key1
import os 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ['OPENAI_API_KEY'] = secret_key1.secretKey()


llm = OpenAI(temperature=0)

def getChatResponse(nation):
    prompt_template_name = PromptTemplate(
        input_variables = ['nation'],
        template = "I want to build a cricket team for real cricket PC game, please give the best 15 players for building {nation} national team."
    )

    nation_chain_name = LLMChain(llm=llm, prompt=prompt_template_name, output_key='15 players')

    prompt_template_team = PromptTemplate(
        input_variables = ['15 players'],
        template = "Please give the playing best 11 out of {15 players} for a match in spinning track. Please name a captain to lead the team. Name the captain in Bold Font"
    )
    team_chain_name = LLMChain(llm=llm, prompt=prompt_template_team, output_key='best 11')

    chain = SequentialChain(
        chains = [nation_chain_name, team_chain_name],
        input_variables=['nation'],
        output_variables = ['15 players', 'best 11']
    )

    response = chain({'nation': nation})
    
    response['nation'] = response['nation'].strip()
    response['15 players'] = response['15 players'].strip()
    response['best 11'] = response['best 11'].strip()

    return response