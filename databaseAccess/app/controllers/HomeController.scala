package controllers

import javax.inject._
import play.api._
import play.api.mvc._

@Singleton
class HomeController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {

  def func1() = Action { implicit request: Request[AnyContent] =>
    Ok("text")
  }

  def func2() = Action { implicit request: Request[AnyContent] =>
    Ok("other text")
  }
  
}
