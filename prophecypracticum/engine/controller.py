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

    def delete_user(self, user_id_to_delete: int) -> int:
        """Delete a user from user list.

        :param user_id_to_delete: The ID that identifies this user in the system.
        :raises: error.IDError
        """
        for the_user in self.users:
            if the_user.my_id == user_id_to_delete:
                self.users.remove(the_user)
                return
        raise error.IDError("Attempted to delete an ID that does not exist.")

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
        raise error.IDError("Attempted to reference an ID that does not exist.")

    def add_supplicant(self, prophet_id: int, supplicant_id: int) -> None:
        """Assign a supplicant to a prophet.

        :param prophet_id: user_id for the prophet - should exist in users.
        :param supplicant_id: user_id for the supplicant - should exist in users.
        """
        if any(supplicant.my_id == supplicant_id for supplicant in self.users):
            prophet = self.get_user(prophet_id)
            prophet.supplicant_id = supplicant_id
            supplicant = self.get_user(supplicant_id)
            supplicant.prophet_id = prophet_id
        else:
            raise error.IDError("Attempted to reference an ID that does not exist.")

    def prophecy_completed_deliver_to_supplicant(self, user_id: int) -> None:
        """Mark prophecy_received as True in supplicant.

        The anticipated flow is that this is a method that will be run when the time for editing prophecies is over.
        If it finds that the prophet has delivered the prophecy, it will mark supplicant's prophecy_received True.
        Then when the email method runs, it will see that this is true and send the email.
        """
        prophet = self.get_user(user_id)
        if prophet.prophecy_given is True:
            supplicant = self.get_user(prophet.supplicant_id)
            supplicant.prophecy_ready_to_read()

    def retrieve_prophecy_for_supplicant(self, supplicant_id: int) -> prophecy.Prophecy:
        """Retrieve prophecy from supplicant's prophet.

        :param supplicant_id: The ID of the user who needs to get their prophecy.
        :returns: A prophecy object.
        """
        supplicant = self.get_user(supplicant_id)
        prophet = self.get_user(supplicant.prophet_id)
        return prophet.get_prophecy()
