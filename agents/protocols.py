from uagents import Model

class MarketDataRequest(Model):
    token: str


class MarketDataResponse(Model):
    token: str
    analysis: str
    status: str


class RiskAssessmentRequest(Model):
    token: str
    analysis: str


class TradeDecision(Model):
    token: str
    action: str
    confidence: float
