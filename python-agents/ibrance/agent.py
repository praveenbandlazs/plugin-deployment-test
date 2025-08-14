from dataiku.llm.python import BaseLLM

class IbranceAgent(BaseLLM):
    def process(self, query, settings, trace):
        user_input = query["messages"][0]["content"].lower()
        if "net sales" in user_input:
            return {"text": "the net sales for Ibrance is $1,200,000"}
        else:
            return {"text": "unknown query for Ibrance insights"}
