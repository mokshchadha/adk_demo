from google.adk import Agent

root_agent = Agent(
    name="PdfProcessor",
    model="gemini-2.0-flash",
    description="You are an expert in parsing pdfs and your job is to create JSON",
    instruction="Convert the PDF into a JSON no need to give any extra explanation just return the JSON"
)