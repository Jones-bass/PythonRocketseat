from .user_register import UserRegister


class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username, email, password) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["email"] = email
        self.registry_user_attributes["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "olaMundo"
    email = "jonesbass.tb@gmail.com"
    password = "myPassword"

    response = controller.registry(username, password, email)

    assert response["type"] == "User"
    assert response["username"] == username
    assert response["email"] == email

    assert repository.registry_user_attributes["email"] == email
    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password