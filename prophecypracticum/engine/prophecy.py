"""A prophecy."""

from datetime import datetime
from prophecypracticum.web.db import db


class Prophecy(db.Model):
    """The Prophecy Object.

    feedback_rating is initialized to 0 as a check of whether feedback has been input.

    :param self.date_of_prophecy: Date and time prophecy is created.
    :param self.prophecy_text: If the prophecy is text, it is stored here.
    :param self.prophecy_photo: If the prophecy is a photo, this is the path to find the photo.
    :param self.feedback_rating: Rating on a scale of 1-5 of how relevant the prophecy was.
    :param self.feedback_text: If feedback was given on the prophecy, store it as text here.
    """

    __tablename__ = "prophecy"

    id = db.Column(db.Integer, primary_key=True)
    prophecy_text = db.Column(db.String(80))
    prophecy_photo = db.Column(db.String(80))
    feedback_rating = db.Column(db.Integer)
    feedback_text = db.Column(db.String(80))
    prophet_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prophet = db.relationship('User')

    def __init__(self, prophecy_text="", prophecy_photo="", feedback_rating=0, feedback_text="", prophet_id=0):
        self.prophecy_text: str = prophecy_text
        self.prophecy_photo: str = prophecy_photo
        self.feedback_rating: int = feedback_rating
        self.feedback_text: str = feedback_text
        self.prophet_id: int = prophet_id
        # date_of_prophecy: datetime

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def get_text_prophecy(self) -> str:
        """Return prophecy text.

        :returns: The text of the prophecy
        """
        return self.prophecy_text

    def modify_text_prophecy(self, prophet_id: int, new_prophecy: str) -> None:
        """Create a new prophecy or modify the text of the prophecy.

        :param new_prophecy: The text of the new prophecy.
        :param prophet_id: The ID of the prophet this prophecy belongs to.
        """
        self.prophet_id = prophet_id
        self.prophecy_text = new_prophecy
        self.save_to_db()

    def get_photo_location(self) -> str:
        """Return photo location on disk.

        :returns: The location of the photo on the disk."""
        return self.prophecy_photo

    def modify_photo_prophecy(self, new_photo_location: str) -> None:
        """Point to a new photo prophecy location.

        :param new_photo_location: The new location for the photo.
        """
        self.prophecy_photo = new_photo_location

    def set_feedback_rating(self, rating: int) -> None:
        """Set feedback rating for the prophecy.

        :param rating: A 1-5 number representing the rating
        """
        self.feedback_rating = rating

    def get_feedback_rating(self) -> int:
        """Return the feedback rating.

        :returns: The feedback rating.
        """
        return self.feedback_rating

    def set_feedback_text(self, new_feedback_text: str) -> None:
        """Set feedback text.

        :param new_feedback_text: Feedback text for the prophecy.
        """
        self.feedback_text = new_feedback_text

    def get_feedback_text(self) -> str:
        """Return feedback text.

        :returns: Feedback text.
        """
        return self.feedback_text
