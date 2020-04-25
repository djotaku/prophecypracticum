"""A user participating in the Prophecy Practicum."""

import attr
from typing import Any
from datetime import datetime

from . import prophecy


@attr.s(auto_attribs=True)
class User:
    """The user participating in the Prophecy Practicum.

    :param self.name: Name of the user participating in the practicum.
    :param self.email: Email address of the user participating in the practicum.
    :param self.user_id: The users ID in the database.
    :param self.prophecy_given: A boolean that stores whether the prophecy has been recorded.
    :param self.prophecy_received_and_interacted: A boolean that stores whether this user has interacted with the \
    prophecy they received.
    """
    name: str
    email: str
    my_id: int = 0
    supplicant_id: int = 0
    prophecy_given: bool = False
    prophecy_received: bool = False
    prophecy_received_and_interacted: bool = False

    def get_email_address(self) -> str:
        """Return user's email address.

        :returns: The user's email address."""
        return self.email

    def create_prophecy(self, prophetic_words: str = "", photo_location: str = "") -> None:
        """Create a prophecy object.

        Should also set self.prophecy_given to True.

        :param prophetic_words: The text of the prophecy.
        :param photo_location: The location of a photo prophecy.
        """
        now = datetime.now()
        if prophetic_words != "":
            prophecy.Prophecy(now, prophecy_text=prophetic_words)
            self.prophecy_given = True
        elif photo_location != "":
            prophecy.Prophecy(now, prophecy_photo=photo_location)
            self.prophecy_given = True
        else:
            print("Invalid, neither text nor photo entered.")

    def set_supplicant_id(self, supplicant_id:int) -> None:
        """Sets the supplicant id number.

        :param supplicant_id: The id number for the supplicant.
        """
        self.supplicant_id = supplicant_id

    def get_supplicant_id(self) -> int:
        """Returns the supplicant ID.

        :returns: Supplicant ID"""
        return self.supplicant_id

    def set_user_id(self, user_id: int) -> None:
        """Set this user's ID

        :param user_id: The ID that will identify this user.
        """
        self.my_id = user_id

    def get_user_id(self) -> int:
        """Return the user ID

        :returns: The user's ID
        """
        return self.my_id

    def is_practicum_complete(self) -> bool:
        """Determine whether the practicum is complete.

        :returns: True if completed and false if any step is incomplete.
        """
        return self.prophecy_given and self.prophecy_received and self.prophecy_received_and_interacted

    def prophecy_ready_to_read(self) -> None:
        """Let the user know there is a prophecy to read"""
        self.prophecy_received = True

    def change_email_address(self, new_email: str) -> None:
        """Allow the user to update their email address.

        :param new_email: The new email address to associate with the user.
        """
        self.email = new_email

    def change_name(self, new_name: str) -> None:
        """Allow the user to update their name.

        :param new_name: The new name to associate with this user.
        """
        self.name = new_name