import pytest
from linked_list import LinkedList  # Assuming linked_list.py contains LinkedList class

@pytest.fixture
def empty_list():
    """Returns an empty LinkedList."""
    return LinkedList()

@pytest.fixture
def small_list():
    """Returns a LinkedList with some initial values."""
    ll = LinkedList()
    count = 0
    while count < 20:
        ll.append(count)
        count += 1
    return ll

def test_append(small_list):
    small_list.append(4)
    assert small_list.length() == 21
    assert small_list.value_at(20) == 4

def test_push_front(small_list):
    small_list.push_front(0)
    assert small_list.value_at(0) == 0
    assert small_list.length() == 21

def test_remove_last(small_list):
    small_list.remove_last()
    assert small_list.length() == 19
    assert small_list.value_at(1) == 1

def test_remove_last_on_empty(empty_list):
    empty_list.remove_last()  # Should not raise error
    assert empty_list.length() == 0

def test_remove_front(small_list):
    small_list.remove_front()
    assert small_list.length() == 19
    assert small_list.value_at(0) == 1

def test_remove_front_on_empty(empty_list):
    empty_list.remove_front()  # Should not raise error
    assert empty_list.length() == 0

def test_value_at(small_list):
    assert small_list.value_at(19) == 19

def test_value_at_out_of_bounds(small_list):
    with pytest.raises(IndexError, match="Out of range"):
        small_list.value_at(21)

def test_insert(small_list):
    small_list.insert(1, 5)
    assert small_list.value_at(1) == 5
    assert small_list.length() == 21

def test_insert_out_of_bounds(small_list):
    with pytest.raises(IndexError, match="Out of range"):
        small_list.insert(25, 100)

def test_remove(small_list):
    small_list.remove(1)
    assert small_list.length() == 19
    assert small_list.value_at(1) == 2

def test_remove_out_of_bounds(small_list):
    with pytest.raises(IndexError, match="Out of range"):
        small_list.remove(25)

def test_reverse(small_list):
    small_list.reverse()
    assert small_list.value_at(0) == 19
    assert small_list.value_at(1) == 18
    assert small_list.value_at(2) == 17

def test_reverse_empty(empty_list):
    empty_list.reverse()  # Should not raise error
    assert empty_list.length() == 0

def test_remove_on_empty(empty_list):
    with pytest.raises(IndexError, match="Out of range"):
        empty_list.remove(0)

def test_remove_only_element():
    ll = LinkedList()
    ll.append(1)
    ll.remove(0)
    assert ll.length() == 0
    assert ll.head is None

def test_reverse_single_element():
    ll = LinkedList()
    ll.append(1)
    ll.reverse()
    assert ll.value_at(0) == 1

if __name__ == "__main__":
    pytest.main()