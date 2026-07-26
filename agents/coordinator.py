from uagents import Agent, Context

from config import (
    COORDINATOR_NAME,
    COORDINATOR_SEED,
)

from agents.protocols import MarketDataResponse

coordinator = Agent(
    name=COORDINATOR_NAME,
    seed=COORDINATOR_SEED,
)

print("Agentic Finance Network")
print("Coordinator Agent Started")
print(f"Address: {coordinator.address}")


@coordinator.on_message(model=MarketDataResponse)
async def handle_market_response(
    ctx: Context,
    sender: str,
    msg: MarketDataResponse,
):
    print("\n[Coordinator] Market Report")
    print(f"Token     : {msg.token}")
    print(f"Analysis  : {msg.analysis}")
    print(f"Status    : {msg.status}\n")


if __name__ == "__main__":
    coordinator.run()
