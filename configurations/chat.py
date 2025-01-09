from autogen import Cache
from configurations.config import az_assistant_agent,code_writer_agent, code_executor_agent, code_executor_agent_gap, code_writer_gap_agent
from configurations.conversable import get_execution_results, get_gap_results
from configurations.conversable import executor, executor_dtf
from prompts.prompts import az_assessment_question, code_executor_question, code_executor_gap_question

def conversable_agnet_chat_gap_calculations(question, agentexecutor):
    get_gap_results(agentexecutor)
    chat_result_gap = code_executor_agent_gap.initiate_chat(
        code_writer_gap_agent,
        message=question,
        summary_method="reflection_with_llm",
    )
    return chat_result_gap

def conversable_agnet_chat(urls, question, agentexecutor):
    get_execution_results(urls, agentexecutor)
    chat_result = code_executor_agent.initiate_chat(
        code_writer_agent,
        message=question,
        summary_method="reflection_with_llm",
    )
    gap_findings = conversable_agnet_chat_gap_calculations(code_executor_gap_question, executor_dtf)
    return gap_findings

def rag_assistant_initiate_chat(rag_proxy_agent, assessment_agent, question):
    with Cache.disk() as cache:
        response = rag_proxy_agent.initiate_chat(
            assessment_agent,
            problem=question,
            n_results=1,
            message=rag_proxy_agent.message_generator,
            max_turns=1
        )

    with open("full_chat_history.txt", "w") as f1:
        f1.write(str(response.chat_history))

    survey_response = next((
        item['content'] for item in response.chat_history
        if 'az_assistant_agent' in item['name']
    ), None)

    result_dict = {}
    for line in survey_response.splitlines():
        key, filename, url = line.split(",")
        if key not in result_dict:
            result_dict[key] = {}
        result_dict[key][filename] = url
    url_list = [url for key in result_dict for url in result_dict[key].values()]
    chat_download_resp = conversable_agnet_chat(url_list, code_executor_question, executor)
    return chat_download_resp


def conversable_agnet_chat_gap_calculations(question, agentexecutor):
    get_gap_results(agentexecutor)
    chat_result_gap = code_executor_agent_gap.initiate_chat(
        code_writer_gap_agent,
        message=question,
        summary_method="reflection_with_llm",
    )
    return chat_result_gap

