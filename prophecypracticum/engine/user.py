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
