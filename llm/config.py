from autogen import config_list_from_json, Cache

def initialize_llm_config(timeout=600, temperature=0.9):
    llm_config = {
        'config_list': config_list_from_json(
            env_or_file="OAI_CONFIG_LIST",
            filter_dict={
                "model": ["gpt-4-turbo"]
            }
        ),
        'timeout': timeout,
        "temperature": temperature
    }
    return llm_config