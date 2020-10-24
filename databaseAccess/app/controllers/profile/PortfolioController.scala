package controllers

import javax.inject._
import play.api._
import play.api.mvc._

@Singleton
class PortfolioController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {

  def getPortfolio(id: String) = Action { implicit request: Request[AnyContent] =>
    Ok(s"Portfolio Object for id $id")
  }
  
}
