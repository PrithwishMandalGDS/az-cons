from autogen import Agent
from agents.worker.analyse_agent import AnalyseWorker
from agents.worker.prompt_analyse import AnalysePrompt

class ControllerAgent(Agent):
    def __init__(self, name):
        super().__init__(name=name)

    def communicate_with_worker(self, term):
        worker = AnalyseWorker(name="AnalyseWorker")
        analyser = AnalysePrompt(name="AnalysePrompt")
        prompt_result = analyser.process_data(term)
        print(f"ControllerAgent: Communicating with worker agent GAP Agent")
        result = worker.process_data()
        return result

