from dataiku.llm.agent_tools import BaseAgentTool

class DummyTool(BaseAgentTool):
    def set_config(self, config, plugin_config):
        self.config = config
        self.plugin_config = plugin_config

    def get_descriptor(self, tool):
        return {
            "description": "A dummy tool that returns a fixed message.",
            "inputSchema": {
                "title": "Dummy Tool Input",
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Optional message to return"
                    }
                },
                "required": []
            }
        }

    def invoke(self, input, trace):
        args = input.get("input", {})
        message = args.get("message", "This is a dummy tool output")
        return {
            "output": message,
            "sources": [{
                "toolCallDescription": "Dummy tool invoked"
            }]
        }
