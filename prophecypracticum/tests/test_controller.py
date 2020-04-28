"""Test controller methods."""

import pytest

from prophecypracticum.engine import controller
from prophecypracticum.engine import error


def test_create_user():
    """The system needs to create users."""
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    assert my_controller.users[0].name == "John"


def test_get_user_by_id():
    """The system should be able to retrieve user by ID.

    Do not check by name because name can be changed.
    """
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    the_user = my_controller.get_user(1)
    assert the_user.my_id == 1


def test_get_user_by_id_bad_id():
    """The system should be able to retrieve user by ID.

    Do not check by name because name can be changed.
    """
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    with pytest.raises(error.IDError):
        my_controller.get_user(2)


def test_assign_supplicant():
    """The system needs to assign a supplicant to a user."""
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    my_controller.create_user("Matthew", "andrew@taxcollectors.com", 3)
    my_controller.add_supplicant(1, 3)
    assert my_controller.users[0].supplicant_id == 3
    assert my_controller.users[2].prophet_id == 1


def test_assign_supplicant_bad_prophet():
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    with pytest.raises(error.IDError):
        my_controller.add_supplicant(3, 2)


def test_assign_supplicant_bad_supplicant():
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    with pytest.raises(error.IDError):
        my_controller.add_supplicant(1, 3)


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
    """The system checks a user to see that a prophecy has been written and changed prophecy_received in supplicant."""
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    john = my_controller.get_user(1)
    andrew = my_controller.get_user(2)
    john.prophecy_given = True
    john.supplicant_id = 2
    my_controller.prophecy_completed_deliver_to_supplicant(1)
    assert andrew.prophecy_received is True


def test_user_reads_prophecy():
    """The system allows the user to read their prophecy.

    Usually I make sure that each unit test stands COMPLETELY alone and doesn't depend on anything else working.
    But in this case, I think that would be a bit over-complicated. Also, by doing TDD, we will know something
    has broken by other tests failing as well. (I hope).

    In essence this is closer to an integration test.
    """
    my_controller = controller.Controller()
    my_controller.create_user("John", "john@fishermen.com", 1)
    my_controller.create_user("Andrew", "andrew@fishermen.com", 2)
    john = my_controller.get_user(1)
    john.create_prophecy(prophetic_words="There will be 10 more of us.")
    my_controller.add_supplicant(1, 2)
    my_controller.prophecy_completed_deliver_to_supplicant(1)
    the_prophecy = my_controller.retrieve_prophecy_for_supplicant(2)
    assert the_prophecy.get_text_prophecy() == "There will be 10 more of us."


def test_supplicant_reviews_prophecy_and_that_is_delivered_to_prophet():
    pass


def test_prophet_reads_review():
    pass


def test_supplicant_reads_previous_prophecy():
    pass


# moderator actions

