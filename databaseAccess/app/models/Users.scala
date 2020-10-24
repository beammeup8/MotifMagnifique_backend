package models
import models.Portfolio

case class User(
  id: String,
  firstName: String,
  lastName: String,
  following: List[User] = Nil,
  follows: List[User] = Nil,
  portfolios: List[Portfolio] = Nil
)