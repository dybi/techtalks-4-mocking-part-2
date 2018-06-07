from assertpy import assert_that
from mock import patch

from person import Person


@patch("person.introduce_myself")
def test_make_friends(mocked_introduce_function):
    greeting = "howdy!"
    mocked_introduce_function.return_value = greeting
    p = Person("Borat")
    assert_that(p.make_freinds()).is_equal_to(greeting)
