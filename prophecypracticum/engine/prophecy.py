"""A prophecy."""

import attr
from datetime import datetime


@attr.s(auto_attribs=True)
class Prophecy:
    """The Prophecy Object.

    feedback_rating is initialized to 0 as a check of whether feedback has been input.

    :param self.date_of_prophecy: Date and time prophecy is created.
    :param self.prophecy_text: If the prophecy is text, it is stored here.
    :param self.prophecy_photo: If the prophecy is a photo, this is the path to find the photo.
    :param self.feedback_rating: Rating on a scale of 1-5 of how relevant the prophecy was.
    :param self.feedback_text: If feedback was given on the prophecy, store it as text here.
    """
    date_of_prophecy: datetime
    prophecy_text: str = ""
    prophecy_photo: str = ""
    feedback_rating: int = 0
    feedback_text: str = ""
