import os
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from backend.prompts.templates import PROMPTS

class ToneConverter:
    def __init__(self):
        # 이제 환경 변수에서 깨끗한 키를 로드합니다.
        self.llm = ChatUpstage(model="solar-pro")

    async def convert(self, text: str, target_audience: str) -> str:
        system_prompt = PROMPTS.get(target_audience, PROMPTS["team"])
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{text}")
        ])
        
        chain = prompt | self.llm
        
        response = await chain.ainvoke({"text": text})
        return response.content
