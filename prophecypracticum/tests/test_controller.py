"""Test controller methods."""

from prophecypracticum.engine import controller


def test_create_user():
    """The system needs to create users."""
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    assert my_controller.users[0].name == "John"


def test_assign_supplicant():
    """The system needs to assign a supplicant to a user."""
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    my_controller.create_user("Matthew", "andrew@taxcollectors.com", 3)
    my_controller.add_supplicant(1, 3)
    assert my_controller.users[0].supplicant_id == 3


def test_email_alert_user_week_has_begun():
    """The system will send an email to the user Sun 1800 letting them know the week's practicum has begun."""
    pass


def test_email_alert_for_incomplete_practicum():
    """The system will send an email to the user Friday 1800 if they have not completed their work.

    This means they both have not made a prophecy and have not provided feedback."""
    pass


def test_email_alert_for_prophecy_ready_for_review():
    """The system will notify the supplicant their prophecy is ready at 1600 Sunday."""
    pass


def test_email_alert_review_feedback():
    """The system will notify the prophet his prophecy review is ready to read."""
    pass


# need to review tardiness criteria again


def test_user_writes_prophecy_and_it_is_delivered_to_supplicant():
    pass


def test_user_reads_prophecy():
    pass


def test_supplicant_reviews_prophecy_and_that_is_delivered_to_prophet():
    pass


def test_prophet_reads_review():
    pass


def test_supplicant_reads_previous_prophecy():
    pass


# moderator actions

