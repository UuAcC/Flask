import pytest
from yandex_testing_lesson import Rectangle


def test_init():
    with pytest.raises(TypeError):
        Rectangle('ads', 4)
    with pytest.raises(TypeError):
        Rectangle(4, 'fdsaf')
    with pytest.raises(ValueError):
        Rectangle(-4, 4)
    with pytest.raises(ValueError):
        Rectangle(4, -4)


def test_s():
    assert Rectangle(4, 4).get_area() == 16


def test_p():
    assert Rectangle(4, 5).get_perimeter() == 20
