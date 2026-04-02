from dotenv import load_dotenv
load_dotenv()

import os
import threading
import time
from google.adk.agents import Agent
from google.adk.tools import FunctionTool, AgentTool

# Directory for the background tasks to write completion statuses
REPORT_DIR = "/tmp/financial_reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def start_financial_report(customer_id: str, quarter: str) -> str:
    """
    Submits a background job to generate a financial report.
    Returns immediately so the user is not blocked.
    """
    report_file = os.path.join(REPORT_DIR, f"{customer_id}_{quarter}.txt")
    
    # Simple deduplication so we don't start it thousands of times
    if os.path.exists(report_file):
        with open(report_file, 'r') as f:
            if f.read().strip() == "PENDING":
                return f"Job for {customer_id} {quarter} is already running."
    
    # Mark as pending
    with open(report_file, 'w') as f:
        f.write("PENDING")
        
    print(f"\n[Job Starter] Dispatched report generation for {customer_id} {quarter}...")
    
    def background_task():
        # Simulate a long-running, 10-second data processing task
        time.sleep(10)
        report_summary = f"Report for {customer_id} for {quarter} is complete. Key finding: Revenue is up 15%."
        
        # Write the final result to the external file
        with open(report_file, 'w') as f:
            f.write(report_summary)
            
        print(f"\n[Background Worker] Generated and saved report to {report_file}")
            
    # Start background task bound to the python process but off the main thread
    threading.Thread(target=background_task, daemon=True).start()
    
    return f"Job successfully dispatched for {customer_id} {quarter}. You can check the status later."

def check_financial_report(customer_id: str, quarter: str) -> str:
    """
    Checks the status and retrieves a generated financial report from the file system.
    """
    report_file = os.path.join(REPORT_DIR, f"{customer_id}_{quarter}.txt")
    
    if not os.path.exists(report_file):
        return f"No report job has been started for {customer_id} {quarter}."
        
    with open(report_file, 'r') as f:
        content = f.read().strip()
        
    if content == "PENDING":
        return f"The report for {customer_id} {quarter} is still processing in the background."
        
    return f"Report complete. Contents: {content}"

# Create standard non-blocking FunctionTools
start_tool = FunctionTool(start_financial_report)
check_tool = FunctionTool(check_financial_report)

# Sub-agent dedicated to launching tasks
starter_agent = Agent(
    name="starter_agent",
    model="gemini-2.5-flash",
    tools=[start_tool],
    instruction="You are responsible for starting financial report generation background jobs when requested by the user."
)

# Sub-agent dedicated to retrieving tasks
checker_agent = Agent(
    name="checker_agent",
    model="gemini-2.5-flash",
    tools=[check_tool],
    instruction="You are responsible for checking the status and retrieving completed financial reports from the system."
)

# Root agent orchestrates workflow
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    tools=[AgentTool(agent=starter_agent), AgentTool(agent=checker_agent)],
    instruction=(
        "You are the main conversational assistant.\n"
        "If the user asks to generate a financial report, delegate to the starter_agent.\n"
        "If the user asks for the status or result of a report, delegate to the checker_agent."
    )
)
