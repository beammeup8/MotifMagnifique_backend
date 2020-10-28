package controllers

import javax.inject._
import play.api._
import play.api.mvc._

@Singleton
class UserController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {

  def getUser(id: String) = Action { implicit request: Request[AnyContent] =>
    Ok(s"User Object for id $id")
  }

  def getSuggestedPortfolios(userId: String) = Action { implicit request: Request[AnyContent] =>
    Ok(s"Portfolios user $userId might like")
  }
  
}
