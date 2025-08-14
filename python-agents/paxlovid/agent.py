from dataiku.llm.python import BaseLLM

class PaxlovidAgent(BaseLLM):
    def process(self, query, settings, trace):
        user_input = query["messages"][0]["content"].lower()
        if "net sales" in user_input:
            return {"text": "the net sales for paxlovid is $1,000,000"}
        else:
            return {"text": "unknown query for paxlovid insights"}
