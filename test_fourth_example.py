import pytest

def sort_by(names, first_letter = False, last_letter = False, length = False):
    if first_letter:
        names.sort()
    if last_letter:
        names.sort(key = lambda name: name[::-1])
    if length:
        names.sort(key = lambda name: len(name))
        # names.sort(key = len)
    return names

class TestSort:
    @pytest.fixture()
    def names(self):
        return ['Ewa', 'Alicja', 'Pawel', 'Mateusz']

    def test_sort(self, names):
        sorted_names = sort_by(names, first_letter = True)
        assert sorted_names == ['Alicja', 'Ewa', 'Mateusz', 'Pawel']

    def test_sort_reverse(self, names):
        sorted_names = sort_by(names, last_letter = True)
        assert sorted_names == ['Alicja', 'Ewa', 'Pawel', 'Mateusz']

    def test_sort_length(self, names):
        sorted_names = sort_by(names, length=True)
        assert sorted_names == ['Ewa', 'Pawel', 'Alicja', 'Mateusz']

