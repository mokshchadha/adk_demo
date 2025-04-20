from google.adk.agents import LlmAgent
from google.adk.tools import google_search

from .util import load_instruction_from_file


scriptwriter_agent = LlmAgent(
    name="ShortsScriptwriter",
    model="gemini-2.0-flash",
    # tools=[google_search],
    output_key="generated_script" # save result to a state
)

visualizer_agent = LlmAgent(
    name="ShortsVisualizer",
    model="gemini-2.0-flash",
    instruction=load_instruction_from_file("visualizer_instruction.txt"),
    description="Generates visual concepts based on a provided script",
    output_key="visual_concepts"
)

formatter_agent = LlmAgent(
    name="ConceptualFormatter",
    model="gemini-2.0-flash",
    instruction=load_instruction_from_file("conceptual_formatter.txt"),
    description="Generates visual concepts based on a provided script",
    output_key="conceptual_formatter"
)

youtube_shorts_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="youtube_shorts_agent",
    description="You are a ShortForm content genius. An AI specialized in crafting engaging youtube shorts content.",
    instruction=load_instruction_from_file("script_writer_instructions.txt"),
    sub_agents=[
        scriptwriter_agent, visualizer_agent, formatter_agent
        
    ]
)

root_agent = youtube_shorts_agent