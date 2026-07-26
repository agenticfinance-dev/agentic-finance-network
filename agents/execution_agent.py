from uagents import Agent

from config import (
    EXECUTION_AGENT_NAME,
    EXECUTION_AGENT_SEED,
)

execution_agent = Agent(
    name=EXECUTION_AGENT_NAME,
    seed=EXECUTION_AGENT_SEED,
)

print("Execution Agent Started")
print(f"Address: {execution_agent.address}")

if __name__ == "__main__":
    execution_agent.run()
