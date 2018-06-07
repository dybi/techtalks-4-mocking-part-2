from assertpy import assert_that
from mock import patch

from person import Person


@patch("person.introduce_myself")
def test_make_friends(mocked_introduce_function):
    greeting = "howdy!"
    mocked_introduce_function.return_value = greeting
    p = Person("Borat")
    assert_that(p.make_freinds()).is_equal_to(greeting)


@patch('person.Pet')
def test_persons_pet_noise(mock_pet):
    new_noise = "Meeow"
    mock_pet.return_value.make_noise.return_value = new_noise
    person = Person("Catlover")
    assert_that(person.pet.make_noise()).is_equal_to(new_noise)
