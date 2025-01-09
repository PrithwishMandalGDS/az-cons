import autogen

def prompt_analyse(prompt):
    config_list_gpt4 = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST",
    )

    gpt4_config = {
        "seed": 42,
        "temperature": 0,
        "config_list": config_list_gpt4,
    }
    planner = autogen.AssistantAgent(
        name="Planner",
        system_message="""Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.
    The plan may involve an engineer who can write code and a scientist who doesn't write code.
    Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
    """,
        llm_config=gpt4_config,
    )

    user_proxy = autogen.UserProxyAgent(
        name="Admin",
        system_message="An admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
        code_execution_config=False,
        human_input_mode="NEVER",
    )

    engineer = autogen.AssistantAgent(
        name="Engineer",
        llm_config=gpt4_config,
        system_message="""Engineer. You follow an approved plan. You write python/shell code to solve tasks. Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor.
    Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. Check the execution result returned by the executor.
    If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
    """,
    )

    scientist = autogen.AssistantAgent(
        name="Scientist",
        llm_config=gpt4_config,
        system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their abstracts printed. You don't write code.""",
    )

    executor = autogen.UserProxyAgent(
        name="Executor",
        system_message="Executor. Execute the code written by the engineer and report the result.",
        human_input_mode="NEVER",
        code_execution_config={
            "last_n_messages": 3,
            "work_dir": "paper",
            "use_docker": False,
        },
    )

    groupchat = autogen.GroupChat(
        agents=[user_proxy, engineer, scientist, planner, executor],
        messages=[],
        max_round=10,
    )

    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

    previous_state = [
        {
            "content": f"Summarize the sentence provided here - {prompt}",
            "role": "user",
            "name": "Admin",
        },
        {
            "content": """Plan:
1. **Engineer**: Find the keywords of the summarized sentence.
2. **Scientist**: Read the summarized sentence and summarize the key findings.
3. **Engineer**: Remove the unwanted words from the sentence like propositions, adjectives etc using NLP.
4. **Scientist**: Provide the one word that is the most important in the sentence.
5. **Engineer**: Develop a prototype or proof of concept to demonstrate how the important word can be taken as a string variable.
6. **Scientist**: Evaluate the prototype, provide feedback, and suggest any improvements or modifications.
7. **Engineer**: Make necessary revisions based on the scientist's feedback and finalize it. 
8. **Admin**: Review the final result and approve for further development or implementation.

Feedback from admin and critic is needed for further refinement of the plan.""",
            "role": "user",
            "name": "Planner",
        },
        {"content": "Agree", "role": "user", "name": "Admin"},
        {
            "content": "Great! Let's proceed with the plan outlined earlier. I will start updating the variable. I will keep you updated on our progress.",
            "role": "user",
            "name": "Planner",
        },
    ]

    last_agent, last_message = manager.resume(messages=previous_state)
    result = last_agent.initiate_chat(recipient=manager, message=last_message, clear_history=False)
    print(result.chat_history)
    important_phrase = ""
    for message in result.chat_history:
        if "The key term in the sentence is:" in message['content']:
            important_phrase = message['content'].split(":")[-1].strip()
    print(important_phrase)
    return important_phrase
