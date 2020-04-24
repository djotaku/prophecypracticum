"""A user participating in the Prophecy Practicum."""

import attr
from typing import Any


@attr.s
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
    user_id: int
    prophecy_given: bool = False
    prophecy_received_and_interacted: bool = False
