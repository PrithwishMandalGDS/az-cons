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