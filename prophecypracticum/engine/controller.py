"""Controls the engine that drives the backend for this project."""

import typing

from . import user
from . import prophecy


class Controller:
    users: typing.List[user.User] = []

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
        for prophet in self.users:
            if prophet.my_id == prophet_id:
                prophet.supplicant_id = supplicant_id
                break
            else:
                print("I will change this in the future to raise an exception because it should never happen")
