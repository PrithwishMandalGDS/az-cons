from agents.default.AgentUserProxy import AZSRAGProxyAgent
from agents.default.AgentAssistant import AZSAssistantAgent
from agents.default.AgentConversable import ConversableAgentFactory
from llm.config import initialize_llm_config
from retriever.config import initialize_config
from prompts.prompts import az_assessment_system_message
from configurations.conversable import code_writer_system_message, executor, executor_dtf, code_writer_gap_system_message
from autogen import ConversableAgent

update_context = True
chunk_token_size = 6000
n_results = 5
docs_path = ["./dataset/azassement.csv"]
get_or_create = True
overwrite = True
custom_timeout = 600
custom_temperature = 0.9
inventory_path = "tmp/chromaDB/az"

llm_config = initialize_llm_config(timeout=custom_timeout, temperature=custom_temperature)
az_assessment_config = initialize_config(chunk_token_size, docs_path, n_results, get_or_create, overwrite, update_context, inventory_path)

az_rag_agent = AZSRAGProxyAgent(
    name="az_rag_agent",
    human_input_mode="NEVER",
    llm_config=llm_config,
    retrieve_config=az_assessment_config,
    code_execution_config=False,
).create_agent()

az_assistant_agent = AZSAssistantAgent(
    name="az_assistant_agent",
    system_message=az_assessment_system_message,
    llm_config=llm_config
).create_agent()

code_writer_agent = ConversableAgent(
    name = "code_writer",
    system_message=code_writer_system_message,
    llm_config=llm_config,
    code_execution_config=False,
    max_consecutive_auto_reply=2,
    human_input_mode="NEVER",
)

code_writer_gap_agent = ConversableAgent(
    name = "code_gap_writer",
    system_message=code_writer_gap_system_message,
    llm_config=llm_config,
    code_execution_config=False,
    max_consecutive_auto_reply=2,
    human_input_mode="NEVER",
)

code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={
        "executor": executor,
    },
    human_input_mode="NEVER",
)

code_executor_agent_gap = ConversableAgent(
    name="code_executor_agent_gap",
    llm_config=False,
    code_execution_config={
        "executor": executor_dtf,
    },
    human_input_mode="NEVER",
)

