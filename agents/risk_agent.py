from uagents import Agent

from config import (
    RISK_AGENT_NAME,
    RISK_AGENT_SEED,
)

risk_agent = Agent(
    name=RISK_AGENT_NAME,
    seed=RISK_AGENT_SEED,
)

print("Risk Agent Started")
print(f"Address: {risk_agent.address}")

if __name__ == "__main__":
    risk_agent.run()
