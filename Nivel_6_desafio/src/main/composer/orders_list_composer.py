from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.orders_list_controller import OrdersListController
from src.views.orders_list_view import OrdersListView


def orders_list_composer():
    conn = db_connection_handler.get_connection()
    model = OrdersRepository(conn)
    controller = OrdersListController(model)
    view = OrdersListView(controller)

    return view