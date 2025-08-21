from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Engineer-Improve-Prompt")

@mcp.tool()
def improve_engineering_prompt(original_prompt: str) -> str:
    """
    Improves an engineering prompt to make it clearer, more specific, and more effective.
    
    Args:
        original_prompt: The original prompt text to improve
        
    Returns:
        An improved version of the prompt with better structure and clarity
    """
    
    improved = f"""
## Goal
{original_prompt}

## Background
[Provide context about the system, codebase, or problem domain]

## Requirements
- Clear, testable requirements
- Specific technical constraints
- Performance or quality criteria

## Technical Approach
1. First, analyze the existing codebase structure
2. Implement changes following TDD methodology
3. Ensure all tests pass before proceeding
4. Document significant decisions

## Success Criteria
- All unit tests passing
- Code follows established patterns
- Documentation updated
- No regression in existing functionality

## Process Guidelines
- Use `plan.md` as the central task tracking document
- Write tests before implementation (TDD)
- Keep the codebase in a working state at all times
- Request review after each major milestone
"""
    
    return improved

@mcp.prompt("Improve the prompt for an engineering task")
def improve_prompt_template() -> str:
    """
    Returns a template for improving engineering prompts.
    """
    
    return """
    You are a prompt engineering expert. Your task is to improve the following prompt to make it clearer, more specific, and more effective. 

    IMPORTANT RULES:
    - Output ONLY the improved prompt, nothing else
    - Make the prompt more specific and actionable
    - Ensure the prompt will produce better results

    Original prompt:
    {USER_INPUT}

    Improved prompt:
    [Provide the enhanced version here]
    """

if __name__ == "__main__":
   mcp.run()