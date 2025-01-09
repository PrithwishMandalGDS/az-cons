from autogen import ConversableAgent

class ConversableAgentFactory:
    def __init__(self, default_llm_config=None, default_code_execution_config=None):
        self.default_llm_config = default_llm_config or {}
        self.default_code_execution_config = default_code_execution_config or {}

    def create_agent(self, name, system_message=None, llm_config=None, code_execution_config=None, max_consecutive_auto_reply=1, human_input_mode="NEVER"):
        agent = ConversableAgent(
            name=name,
            system_message=system_message,
            llm_config=llm_config or self.default_llm_config,
            code_execution_config=code_execution_config or self.default_code_execution_config,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            human_input_mode=human_input_mode,
        )
        return agent