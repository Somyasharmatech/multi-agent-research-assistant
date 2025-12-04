from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings

class CriticAgent:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0, 
            model_name=settings.MODEL_NAME, 
            api_key=settings.GROQ_API_KEY
        )
        
    def critique(self, answer, context):
        """
        Critiques the answer based on the provided context.
        Returns a corrected or validated answer.
        """
        system = "You are a critical reviewer. Your job is to check if the provided answer is supported by the context. Remove any hallucinations or unsupported claims. If the answer is good, return it as is. If not, rewrite it using ONLY the context."
        human = "Context:\n{context}\n\nAnswer:\n{answer}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        
        chain = prompt | self.llm
        response = chain.invoke({"context": context, "answer": answer})
        return response.content

if __name__ == "__main__":
    critic = CriticAgent()
    # print(critic.critique("Quantum computers use magic.", "Quantum computers use qubits."))
