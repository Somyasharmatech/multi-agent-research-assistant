from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.retriever import RetrieverAgent
from agents.critic import CriticAgent
from agents.writer import WriterAgent
import os

class ResearchAssistant:
    def __init__(self):
        self.planner = PlannerAgent()
        self.search_agent = SearchAgent()
        self.retriever = RetrieverAgent()
        self.critic = CriticAgent()
        self.writer = WriterAgent()
        
    def run_research(self, query):
        """
        Executes the full research pipeline.
        """
        print(f"Starting research for: {query}")
        
        # 1. Plan
        sub_tasks = self.planner.plan_research(query)
        print(f"Plan: {sub_tasks}")
        
        sections = []
        
        for task in sub_tasks:
            print(f"\nProcessing sub-task: {task}")
            
            # 2. Search
            raw_text = self.search_agent.search_and_scrape([task])
            
            # 3. Index
            self.retriever.index_content(raw_text)
            
            # 4. Retrieve
            relevant_chunks = self.retriever.retrieve(task)
            context = "\n\n".join(relevant_chunks)
            
            # 5. Write Draft
            draft_section = self.writer.write_section(task, context)
            
            # 6. Critique
            critiqued_section = self.critic.critique(draft_section, context)
            
            sections.append(f"## {task}\n\n{critiqued_section}")
            
        # 7. Compile
        final_report = self.writer.compile_report(sections)
        return final_report

if __name__ == "__main__":
    # Example usage
    assistant = ResearchAssistant()
    report = assistant.run_research("Explain Quantum Computing and compare it with Classical Computing.")
    print(report)
    
    # Save report
    with open("research_report.md", "w", encoding="utf-8") as f:
        f.write(report)
