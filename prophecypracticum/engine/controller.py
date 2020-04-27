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

    def get_user(self, user_to_get: int) -> user.User:
        """Return the user requested by ID.

        If the user cannot be found, raise an exception because this is automated so it should never be a bad number.

        :param user_to_get: The user ID of the user to get.
        :raises: error.IDError
        :returns: The requested user.
        """
        for the_user in self.users:
            if the_user.my_id == user_to_get:
                return the_user
            else:
                raise error.IDError("Attempted to reference an ID that does not exist.")

    def add_supplicant(self, prophet_id: int, supplicant_id: int) -> None:
        """Assign a supplicant to a prophet.

        :param prophet_id: user_id for the prophet - should exist in users.
        :param supplicant_id: user_id for the supplicant - should exist in users.
        """
        if any(supplicant.my_id == supplicant_id for supplicant in self.users):
            prophet = self.get_user(prophet_id)
            prophet.supplicant_id = supplicant_id
        else:
            raise error.IDError("Attempted to reference an ID that does not exist.")
