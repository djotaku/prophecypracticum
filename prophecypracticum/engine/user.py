"""A user participating in the Prophecy Practicum."""

from datetime import datetime

from . import prophecy
from prophecypracticum.web.db import db


class User(db.Model):
    """The user participating in the Prophecy Practicum.

    :param self.name: Name of the user participating in the practicum.
    :param self.email: Email address of the user participating in the practicum.
    :param self.supplicant_id: The ID of this prophet's supplicant
    :param self.prophet_id: The ID of this supplicant's prophet.
    :param self.prophecy_given: A boolean that stores whether the prophecy has been recorded.
    :param self.prophecy_received: Marked True when prophecy is ready to read.
    :param self.prophecy_received_and_interacted: A boolean that stores whether this user has interacted with the \
    prophecy they received.
    :param self.this_week_prophecy: This week's prophecy.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))
    supplicant_id = db.Column(db.Integer)
    prophet_id = db.Column(db.Integer)

    def __init__(self, name, password, email, supplicant_id=0, prophet_id=0):
        self.name: str = name
        self.password = password
        self.email: str = email
        self.supplicant_id = supplicant_id
        self.prophet_id: int = prophet_id
        self.prophecy_given: bool = False
        self.prophecy_received: bool = False
        self.prophecy_received_and_interacted: bool = False
        self.this_week_prophecy: prophecy.Prophecy = None

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, the_id):
        return cls.query.filter_by(id=the_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

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
            self.this_week_prophecy = prophecy.Prophecy(now, prophecy_text=prophetic_words)
            self.prophecy_given = True
        elif photo_location != "":
            self.this_week_prophecy = prophecy.Prophecy(now, prophecy_photo=photo_location)
            self.prophecy_given = True
        else:
            print("Invalid, neither text nor photo entered.")

    def get_prophecy(self) -> prophecy.Prophecy:
        """Return a prophecy object.

        Need to change to get previous prophecies, but how to do that depends on how many weeks will be kept.

        :returns: A prophecy object.
        """
        return self.this_week_prophecy

    def set_supplicant_id(self, supplicant_id: int) -> None:
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
        self.id = user_id

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