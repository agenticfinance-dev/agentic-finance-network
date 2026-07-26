from uagents import Agent, Context

from config import (
    MARKET_AGENT_NAME,
    MARKET_AGENT_SEED,
)

from agents.protocols import (
    MarketDataRequest,
    MarketDataResponse,
)

market_agent = Agent(
    name=MARKET_AGENT_NAME,
    seed=MARKET_AGENT_SEED,
)

print("Market Agent Started")
print(f"Address: {market_agent.address}")


@market_agent.on_message(model=MarketDataRequest)
async def handle_market_request(
    ctx: Context,
    sender: str,
    msg: MarketDataRequest,
):
    response = MarketDataResponse(
        token=msg.token,
        analysis="Market trend is BULLISH",
        status="SUCCESS",
    )

    await ctx.send(sender, response)


if __name__ == "__main__":
    market_agent.run()
