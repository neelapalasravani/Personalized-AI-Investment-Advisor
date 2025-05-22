from langchain_together import ChatTogether
from langchain.schema import HumanMessage, SystemMessage

def get_llm_instances(api_key):
    return {
        "Llama-3.3-70B": ChatTogether(
            together_api_key=api_key,
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
        ),
        "Mistral-7B": ChatTogether(
            together_api_key=api_key,
            model="mistralai/Mistral-7B-Instruct-v0.3"
        )
    }
