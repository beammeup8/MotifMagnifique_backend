package models
import scala.math.BigDecimal

case class Stock(
  code: String,
  name: String,
  currentPrice: BigDecimal,
  change: Double
)