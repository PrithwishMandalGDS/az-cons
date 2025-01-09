from autogen import Agent
from configurations.chat import rag_assistant_initiate_chat, conversable_agnet_chat, conversable_agnet_chat_gap_calculations
from configurations.config import az_assistant_agent, az_rag_agent
from prompts.prompts import az_assessment_question, code_executor_question, code_executor_gap_question
from configurations.conversable import executor, executor_dtf

class AnalyseWorker(Agent):
    def __init__(self, name):
        super().__init__(name=name)

    def process_data(self):
        response_msg = rag_assistant_initiate_chat(az_rag_agent, az_assistant_agent, az_assessment_question)
        return response_msg