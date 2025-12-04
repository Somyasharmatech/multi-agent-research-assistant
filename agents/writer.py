from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings

class WriterAgent:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.5, 
            model_name=settings.MODEL_NAME, 
            api_key=settings.GROQ_API_KEY
        )
        
    def write_section(self, topic, context):
        """
        Writes a section of the report based on the topic and context.
        """
        system = "You are a technical writer. Write a detailed and accurate section for a research report based on the provided context. Cite sources if available in the text."
        human = "Topic: {topic}\n\nContext:\n{context}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        
        chain = prompt | self.llm
        response = chain.invoke({"topic": topic, "context": context})
        return response.content
        
    def compile_report(self, sections):
        """
        Compiles the final report from sections.
        """
        report = "# Research Report\n\n"
        for section in sections:
            report += section + "\n\n"
        return report

if __name__ == "__main__":
    writer = WriterAgent()
    # print(writer.write_section("Introduction", "Context..."))
