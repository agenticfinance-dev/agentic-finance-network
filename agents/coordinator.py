from uagents import Agent, Context

from config import (
    COORDINATOR_NAME,
    COORDINATOR_SEED,
)

from agents.market_agent import market_agent
from agents.risk_agent import risk_agent
from agents.execution_agent import execution_agent

from agents.protocols import (
    MarketDataRequest,
    MarketDataResponse,
    RiskAssessmentRequest,
    TradeDecision,
    ExecutionResult,
)

coordinator = Agent(
    name=COORDINATOR_NAME,
    seed=COORDINATOR_SEED,
)

print("Agentic Finance Network")
print("Coordinator Agent Started")
print(f"Address: {coordinator.address}")


@coordinator.on_event("startup")
async def startup(ctx: Context):
    print("[Coordinator] Startup event triggered")

    await ctx.send(
        market_agent.address,
        MarketDataRequest(token="BTC")
    )


@coordinator.on_message(model=MarketDataResponse)
async def handle_market_response(
    ctx: Context,
    sender: str,
    msg: MarketDataResponse,
):
    print("\n[Coordinator] Market Report")
    print(f"Token: {msg.token}")
    print(f"Analysis: {msg.analysis}")
    print(f"Status: {msg.status}")

    await ctx.send(
        risk_agent.address,
        RiskAssessmentRequest(
            token=msg.token,
            analysis=msg.analysis,
        ),
    )


@coordinator.on_message(model=TradeDecision)
async def handle_trade_decision(
    ctx: Context,
    sender: str,
    msg: TradeDecision,
):
    print("\n[Coordinator] Trade Decision")
    print(f"Token: {msg.token}")
    print(f"Action: {msg.action}")
    print(f"Confidence: {msg.confidence}")

    await ctx.send(
        execution_agent.address,
        msg,
    )


@coordinator.on_message(model=ExecutionResult)
async def handle_execution_result(
    ctx: Context,
    sender: str,
    msg: ExecutionResult,
):
    print("\n[Coordinator] Execution Result")
    print(f"Token: {msg.token}")
    print(f"Action: {msg.action}")
    print(f"Status: {msg.status}")
    print(f"Message: {msg.message}")


if __name__ == "__main__":
    coordinator.run()
