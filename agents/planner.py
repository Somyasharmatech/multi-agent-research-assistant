from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings
import json

class PlannerAgent:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0, 
            model_name=settings.MODEL_NAME, 
            api_key=settings.GROQ_API_KEY
        )
        
    def plan_research(self, query):
        """
        Breaks down the user query into research sub-tasks.
        """
        system = "You are a research planner. Break down the user query into smaller, actionable research sub-tasks. Return the result as a JSON list of strings."
        human = "Query: {query}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        
        chain = prompt | self.llm
        response = chain.invoke({"query": query})
        
        try:
            # Attempt to parse JSON from the response content
            # This is a basic implementation; for production, use structured output parsers
            content = response.content.strip()
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].strip()
                
            sub_tasks = json.loads(content)
            return sub_tasks
        except Exception as e:
            print(f"Error parsing plan: {e}")
            # Fallback: split by newlines if it looks like a list
            return [line.strip("- *") for line in response.content.split("\n") if line.strip()]

if __name__ == "__main__":
    planner = PlannerAgent()
    print(planner.plan_research("Explain Quantum Computing"))
