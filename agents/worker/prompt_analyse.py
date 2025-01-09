from autogen import Agent
from prompts.prompt_analyse import prompt_analyse

class AnalysePrompt(Agent):
    def __init__(self, name):
        super().__init__(name=name)

    def process_data(self, data):
        result = prompt_analyse(data)
        return result