from dotenv import load_dotenv
load_dotenv()

import time
import uuid
import asyncio
from concurrent.futures import ThreadPoolExecutor
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from google.adk.tools import LongRunningFunctionTool
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

from long_running_agent.agent import root_agent

# --- 4. Simulation of the Non-Blocking Interaction ---

runner = Runner(
    app_name="long_running_demo",
    agent=root_agent,
    session_service=InMemorySessionService(),
    auto_create_session=True
)

def run_main_agent(query: str, session_id: str = "session_1"):
    """Helper function to simulate a call to the main agent."""
    print(f"\n> USER: {query}")
    
    events = runner.run(
        user_id="user_1",
        session_id=session_id,
        new_message=types.Content(role="user", parts=[types.Part.from_text(text=query)])
    )
    
    final_response = ""
    for event in events:
        if event.is_final_response() and event.content:
            text = "".join(part.text for part in event.content.parts if part.text)
            final_response += text
    
    print(f"< MAIN AGENT: {final_response}")

# We use a ThreadPoolExecutor to simulate running the long task in the
# background while the main agent can still take another request.
executor = ThreadPoolExecutor(max_workers=2)

if __name__ == "__main__":
    # --- SCENARIO START ---

    # User asks the main agent to start the long-running task.
    # This will trigger the FinancialSubAgent and its LongRunningFunctionTool.
    # We submit this to the thread pool to run in the "background".
    long_task_future = executor.submit(run_main_agent, "Please generate the Q1 financial report for customer 'ACME Corp'.", "session_1")

    # While the sub-agent is "running" (i.e., time.sleep(10) is active),
    # the user can ask the main agent another, unrelated question.
    print("\n--- Main agent is now free to handle other requests ---")
    time.sleep(2) # Give a moment for the first task to start
    run_main_agent("What is the capital of France?", "session_2")

    # Now, we wait for the long-running task to complete and print its result.
    print("\n--- Waiting for the long-running sub-agent to finish ---")
    long_task_future.result() # This will block until the thread is done.

    print("\n--- SCENARIO END ---")
    executor.shutdown()

