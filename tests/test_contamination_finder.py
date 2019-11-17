import unittest
from unittest.mock import Mock
from src.contamination_finder.contamination_finder import Contamination_Finder

class Test_Contamination_Finder_get_species_most_found_in_unmapped_reads(unittest.TestCase):
    def setUp(self):
        self.bam_record_mock = Mock()
        self.bam_record_mock.get_sequence.return_value = "dummy"

        self.bam_mock = Mock()

        self.index_mock = Mock()

    def test_get_species_most_found_in_unmapped_reads___no_unmapped_reads___returns_None(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = []

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = None
        self.assertEqual(actual, expected)

    def test_get_species_most_found_in_unmapped_reads___one_unmapped_read___returns_Dog(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = [self.bam_record_mock]
        self.index_mock.get_species_for_the_given_sequence.return_value = ["Cat", "Dog", "Dog"]

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = "Dog"
        self.assertEqual(actual, expected)


    def test_get_species_most_found_in_unmapped_reads___three_unmapped_reads___returns_Cat(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = [self.bam_record_mock] * 3
        self.index_mock.get_species_for_the_given_sequence.side_effect = [ # allows us to put several return values
            ["Cat", "Dog", "Dog"], # is returned in the first call
            ["Human", "Human", "Human"], # is returned in the second call
            ["Human", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat"], # is returned in the third call
            ]

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = "Cat"
        self.assertEqual(actual, expected)


    # TODO : exercise: test Contamination_Finder.get_species_most_found_in_unmapped_reads