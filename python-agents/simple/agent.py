from dataiku.llm.python import BaseLLM

class SimpleAgent(BaseLLM):
    def process(self, query, settings, trace):
        return {"text": "unknown user request"}
