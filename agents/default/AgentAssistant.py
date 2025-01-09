from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen import AssistantAgent

class AZSAssistantAgent:
    def __init__(self, name, llm_config, system_message):
        self.name = name
        self.llm_config = llm_config
        self.system_message = system_message

    def create_agent(self):
        return AssistantAgent(
            name=self.name,
            llm_config=self.llm_config,
            system_message=self.system_message,
        )

