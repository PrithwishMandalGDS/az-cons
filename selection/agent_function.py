import os
from typing_extensions import Annotated
from selection.config import user_proxy, engineer
from agents.worker.analyse_agent import AnalyseWorker

# default_path = "backend_dir/"

@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Calling the worker agent")
def agent_call():
    worker = AnalyseWorker("AnalyseWorker")
    worker.process_data()

# @user_proxy.register_for_execution()
# @engineer.register_for_llm(description="Check the contents of a chosen file.")
# def see_file(filename: Annotated[str, "Name and path of file to check."]):
#     with open(default_path + filename, "r") as file:
#         lines = file.readlines()
#     formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
#     file_contents = "".join(formatted_lines)
#
#     return 0, file_contents
#
# @user_proxy.register_for_execution()
# @engineer.register_for_llm(description="Replace old piece of code with new one. Proper indentation is important.")
# def modify_code(
#     filename: Annotated[str, "Name and path of file to change."],
#     start_line: Annotated[int, "Start line number to replace with new code."],
#     end_line: Annotated[int, "End line number to replace with new code."],
#     new_code: Annotated[str, "New piece of code to replace old code with. Remember about providing indents."],
# ):
#     with open(default_path + filename, "r+") as file:
#         file_contents = file.readlines()
#         file_contents[start_line - 1 : end_line] = [new_code + "\n"]
#         file.seek(0)
#         file.truncate()
#         file.write("".join(file_contents))
#     return 0, "Code modified"
#
# @user_proxy.register_for_execution()
# @engineer.register_for_llm(description="Create a new file with code.")
# def create_file_with_code(
#     filename: Annotated[str, "Name and path of file to create."], code: Annotated[str, "Code to write in the file."]
# ):
#     with open(default_path + filename, "w") as file:
#         file.write(code)
#     return 0, "File created successfully"