from uagents import Bureau

from agents.coordinator import coordinator
from agents.market_agent import market_agent
from agents.risk_agent import risk_agent
from agents.execution_agent import execution_agent

from config import APP_NAME, VERSION, DEFAULT_PORT


def main():
    print(f"{APP_NAME} v{VERSION}")
    print("Starting Agentic Finance Network...")

    bureau = Bureau(
        port=DEFAULT_PORT,
        endpoint=[f"http://127.0.0.1:{DEFAULT_PORT}/submit"],
    )

    bureau.add(coordinator)
    bureau.add(market_agent)
    bureau.add(risk_agent)
    bureau.add(execution_agent)

    print("✓ Coordinator added")
    print("✓ Market Agent added")
    print("✓ Risk Agent added")
    print("✓ Execution Agent added")
    print("✓ Bureau ready")

    bureau.run()


if __name__ == "__main__":
    main()
