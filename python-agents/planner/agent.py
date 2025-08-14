from dataiku.llm.python import BaseLLM

class PlannerAgent(BaseLLM):
    def process(self, query, settings, trace):
        prompt = query["messages"][0]["content"].lower()

        if "paxlovid" in prompt:
            route = "paxlovid"
        elif "ibrance" in prompt:
            route = "ibrance"
        else:
            route = "simple"

        return {
            "agent": route,
            "agentInput": query
        }

