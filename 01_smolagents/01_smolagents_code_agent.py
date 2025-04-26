import os
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool# Initialize the Gemini model
model_id = "gemini/gemini-2.0-flash-001"
model = LiteLLMModel(
    model_id=model_id,
    api_key=os.environ.get("GOOGLE_API_KEY", "")
)
search_tool = DuckDuckGoSearchTool()
agent_with_search = CodeAgent(tools=[search_tool], model=model, add_base_tools=True)
agent_with_search.run("""
                      Write user requirements for Cyber Security SOC Software 
                      """)