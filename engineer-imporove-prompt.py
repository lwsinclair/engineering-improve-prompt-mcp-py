from mcp.server.fastmcp import FastMCP
 
 # start mcp server
#.venv/bin/python3 .venv/bin/mcp dev engineer-imporove-prompt.py

 # in mcp-inspector
 # Command: /Users/chungta/development/workspace/experiment/engineering-improve-prompt-mcp-py/run-mcp-server.sh/Users/chungta/development/workspace/experiment/engineering-improve-prompt-mcp-py/run-mcp-server.sh


mcp = FastMCP("Engineer-Improve-Prompt")

@mcp.prompt("Improve the prompt for an engineering task")
def improve_prompt() -> str:
    """
    ARguments: enhance promit
    Returns an enhanced prompt for an engineering task.
    """
    
    return """
    You are a prompt engineering expert. Your task is to improve the following prompt to make it clearer, more specific, and more effective. 

    IMPORTANT RULES:
    - Output ONLY the improved prompt, nothing else
    - Make the prompt more specific and actionable
    - Ensure the prompt will produce better results

    Original prompt:
    Goal:

    ## Background

    ## Requirements

    ## Process
    - Use `plan.md` as the central task-master document. Update it regularly with progress.
    - Agents must record status changes and progress in `plan.md`.
    - Subagents can be assigned to sub-tasks and may work in parallel, provided all requirements above are followed.
    - All code must be written in TDD style. (Write test, see test fail, write code, see test pass,  refactor to tidy up, see test pass, go to next)
    - Subagents may work in parallel, but the codebase must never be in a broken state. (use `mvn clean compile` & `mvn clean test-compile`)
    - After completing each step, stop and wait for the user to give approval or further instructions before proceeding.

    Improved prompt:
    """

if __name__ == "__main__":
   mcp.run()   
    