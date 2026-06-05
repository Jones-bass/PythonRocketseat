from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.orders_create_controller import OrdersCreateController
from src.views.orders_creator_view import OrdersCreatorView

def orders_creator_composer():
    conn = db_connection_handler.get_connection()
    model = OrdersRepository(conn)
    controller = OrdersCreateController(model)
    view = OrdersCreatorView(controller)

    return view

