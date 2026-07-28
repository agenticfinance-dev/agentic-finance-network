from uagents import Agent, Context

from config import (
    RISK_AGENT_NAME,
    RISK_AGENT_SEED,
)

from agents.protocols import (
    RiskAssessmentRequest,
    TradeDecision,
)

risk_agent = Agent(
    name=RISK_AGENT_NAME,
    seed=RISK_AGENT_SEED,
)

print("Risk Agent Started")
print(f"Address: {risk_agent.address}")


@risk_agent.on_message(model=RiskAssessmentRequest)
async def handle_risk_request(
    ctx: Context,
    sender: str,
    msg: RiskAssessmentRequest,
):
    print("\n[Risk Agent] Assessment Request")
    print(f"Token: {msg.token}")
    print(f"Analysis: {msg.analysis}")

    decision = TradeDecision(
        token=msg.token,
        action="BUY",
        confidence=0.90,
    )

    await ctx.send(sender, decision)


if __name__ == "__main__":
    risk_agent.run()
