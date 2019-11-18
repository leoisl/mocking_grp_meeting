import unittest
from unittest.mock import Mock
from src.contamination_finder.contamination_finder import Contamination_Finder

class Test_Contamination_Finder_get_species_most_found_in_unmapped_reads(unittest.TestCase):
    def setUp(self):
        self.bam_record_mock_1 = Mock()
        self.bam_record_mock_1.get_sequence.return_value = "dummy_1"
        self.bam_record_mock_2 = Mock()
        self.bam_record_mock_2.get_sequence.return_value = "dummy_2"
        self.bam_record_mock_3 = Mock()
        self.bam_record_mock_3.get_sequence.return_value = "dummy_3"

        self.bam_mock = Mock()

        self.index_mock = Mock()

    def test_get_species_most_found_in_unmapped_reads___no_unmapped_reads___returns_None(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = []
        self.index_mock.get_species_for_the_given_sequence.return_value = []

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = None
        self.assertEqual(actual, expected)


        # mocking calls asserts
        self.bam_mock.get_all_unmapped_records.assert_called_once()
        # requiring the implementation to not query the index if there is nothing to be queried
        self.index_mock.get_species_for_the_given_sequence.assert_not_called()

    def test_get_species_most_found_in_unmapped_reads___one_unmapped_read___returns_Dog(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = [self.bam_record_mock_1]
        self.index_mock.get_species_for_the_given_sequence.return_value = ["Cat", "Dog", "Dog"]

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = "Dog"
        self.assertEqual(actual, expected)

        # mocking calls asserts
        self.bam_mock.get_all_unmapped_records.assert_called_once()
        self.index_mock.get_species_for_the_given_sequence.assert_called_once_with("dummy_1")


    def test_get_species_most_found_in_unmapped_reads___three_unmapped_reads___returns_Cat(self):
        contamination_finder = Contamination_Finder(self.bam_mock, self.index_mock, None)
        self.bam_mock.get_all_unmapped_records.return_value = [self.bam_record_mock_1, self.bam_record_mock_2, self.bam_record_mock_3]
        self.index_mock.get_species_for_the_given_sequence.side_effect = [ # allows us to put several return values
            ["Cat", "Dog", "Dog"], # is returned in the first call
            ["Human", "Human", "Human"], # is returned in the second call
            ["Human", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat", "Cat"], # is returned in the third call
            ]

        actual = contamination_finder.get_species_most_found_in_unmapped_reads()

        expected = "Cat"
        self.assertEqual(actual, expected)

        # mocking calls asserts
        self.bam_mock.get_all_unmapped_records.assert_called_once()
        self.assertEqual(self.index_mock.get_species_for_the_given_sequence.call_count, 3)
        self.index_mock.get_species_for_the_given_sequence.assert_any_call("dummy_1")
        self.index_mock.get_species_for_the_given_sequence.assert_any_call("dummy_2")
        self.index_mock.get_species_for_the_given_sequence.assert_any_call("dummy_3")


    # TODO : exercise: test Contamination_Finder.get_species_most_found_in_unmapped_reads