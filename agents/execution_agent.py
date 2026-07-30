from uagents import Agent, Context

from config import (
    EXECUTION_AGENT_NAME,
    EXECUTION_AGENT_SEED,
)

from agents.protocols import (
    TradeDecision,
    ExecutionResult,
)

execution_agent = Agent(
    name=EXECUTION_AGENT_NAME,
    seed=EXECUTION_AGENT_SEED,
)

print("Execution Agent Started")
print(f"Address: {execution_agent.address}")


@execution_agent.on_message(model=TradeDecision)
async def handle_trade(
    ctx: Context,
    sender: str,
    msg: TradeDecision,
):
    print("\n[Execution Agent] Trade Request")
    print(f"Token: {msg.token}")
    print(f"Action: {msg.action}")
    print(f"Confidence: {msg.confidence}")

    result = ExecutionResult(
        token=msg.token,
        action=msg.action,
        status="SUCCESS",
        message="Trade executed successfully (simulation)"
    )

    await ctx.send(sender, result)


if __name__ == "__main__":
    execution_agent.run()
