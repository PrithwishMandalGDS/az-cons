from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

class AZSRAGProxyAgent:
    def __init__(self, name, human_input_mode, llm_config, retrieve_config, code_execution_config):
        self.name = name
        self.human_input_mode = human_input_mode
        self.llm_config = llm_config
        self.retrieve_config = retrieve_config
        self.code_execution_config = code_execution_config

    def create_agent(self):
        return RetrieveUserProxyAgent(
            name=self.name,
            human_input_mode=self.human_input_mode,
            llm_config=self.llm_config,
            retrieve_config=self.retrieve_config,
            code_execution_config=self.code_execution_config,
        )
