"""Controls the engine that drives the backend for this project."""

import typing

from . import error
from . import user
from . import prophecy


class Controller:
    def __init__(self):
        self.users: typing.List[user.User] = []

    def create_user(self, username: str, user_email: str, user_id: int) -> None:
        """Create a user and add it to the users list.

        :param username: The user's name
        :param user_email: The user's email address.
        :param user_id: The ID that identifies this user in the system.
        """
        this_user = user.User(username, user_email, user_id)
        self.users.append(this_user)

    def add_supplicant(self, prophet_id: int, supplicant_id: int) -> None:
        """Assign a supplicant to a prophet.

        :param prophet_id: user_id for the prophet - should exist in users.
        :param supplicant_id: user_id for the supplicant - should exist in users.
        """
        print(supplicant_id)
        print(len(self.users))
        for supplicant in self.users:
            print(supplicant)

        for prophet in self.users:
            if prophet.my_id == prophet_id and any(supplicant.my_id == supplicant_id for supplicant in self.users):
                prophet.supplicant_id = supplicant_id
                break
            else:
                raise error.IDError("Attempted to reference an ID that does not exist.")

