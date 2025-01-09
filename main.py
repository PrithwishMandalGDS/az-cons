from agents.orchestrator.master import ControllerAgent
controller = ControllerAgent(name="ControllerAgent")
statement = "I want to find out the gap analysis"
response = controller.communicate_with_worker(statement)

# from fastapi import FastAPI
# from agents.orchestrator.master import ControllerAgent
#
# app = FastAPI()
# controller = ControllerAgent(name="ControllerAgent")
#
# @app.get("/communicate/{worker_name}")
# async def communicate(worker_name: str):
#     response = controller.communicate_with_worker(worker_name)
#     return {"response": response}