from pydantic import BaseModel

from app.core.enums import Sentiment


class SentimentPredictionResult(BaseModel):
    pass