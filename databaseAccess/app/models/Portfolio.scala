package models
import models.Stock

case class Portfolio(
  ownerId: String, 
  stocks: List[Stock]
)