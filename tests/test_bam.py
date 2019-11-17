import unittest
from src.bam.bam import Bam, BamRecord
from pathlib import Path
from pysam import AlignedSegment, AlignmentHeader
from unittest.mock import Mock

# A naming pattern for unit test classes can be:
# Test_<Class_Being_Tested>_<Method_Being_Tested>
class Test_Bam_get_all_records(unittest.TestCase):
    # Base case
    def test_bam_with_no_records___returns_no_records(self):
        bam = Bam(Path("test_data/zero_reads.bam"))

        actual = bam.get_all_records()

        expected = []
        self.assertListEqual(actual, expected)

    # Base case
    def test_bam_with_one_record___returns_one_record(self):
        bam = Bam(Path("test_data/one_read.bam"))

        actual = bam.get_all_records()

        sam_header = AlignmentHeader.from_text("@SQ	SN:chr1_subsampled	LN:2755\n"
                                               "@PG	ID:dummy	PN:dummy	VN:dummy	CL:dummy")
        expected = [BamRecord(AlignedSegment.fromstring("chr1_subsampled_simulated_read_0	0	chr1_subsampled	1	60	100M	*	0	0	ACAAAAAAAACAAAACTTGAGGCCTGGCCTTCTGCTCCTCTCCAACCTCCCCTTCTCTGGGCCCAAGCCACCTTGGCTGAGGAGGGGGCGAGGAGGTGTG	*	NM:i:0	MD:Z:100	AS:i:100	XS:i:0", sam_header))]
        self.assertListEqual(actual, expected)

    # "induction step"
    def test_bam_with_four_records___returns_four_records(self):
        bam = Bam(Path("test_data/four_reads.bam"))

        actual = bam.get_all_records()

        sam_header = AlignmentHeader.from_text("@SQ	SN:chr1_subsampled	LN:2755\n"
                                               "@PG	ID:dummy	PN:dummy	VN:dummy	CL:dummy")
        expected = [
            BamRecord(AlignedSegment.fromstring("chr1_subsampled_simulated_read_0	0	chr1_subsampled	1	60	100M	*	0	0	ACAAAAAAAACAAAACTTGAGGCCTGGCCTTCTGCTCCTCTCCAACCTCCCCTTCTCTGGGCCCAAGCCACCTTGGCTGAGGAGGGGGCGAGGAGGTGTG	*	NM:i:0	MD:Z:100	AS:i:100	XS:i:0", sam_header)),
            BamRecord(AlignedSegment.fromstring("chr1_subsampled_simulated_read_1	0	chr1_subsampled	2	60	100M	*	0	0	CAAAAAAAACAAAACTTGAGGCCTGGCCTTCTGCTCCTCTCCAACCTCCCCTTCTCTGGGCCCAAGCCACCTTGGCTGAGGAGGGGGCGAGGAGGTGTGA	*	NM:i:0	MD:Z:100	AS:i:100	XS:i:0", sam_header)),
            BamRecord(AlignedSegment.fromstring("chr1_subsampled_simulated_read_2	0	chr1_subsampled	3	60	100M	*	0	0	AAAAAAAACAAAACTTGAGGCCTGGCCTTCTGCTCCTCTCCAACCTCCCCTTCTCTGGGCCCAAGCCACCTTGGCTGAGGAGGGGGCGAGGAGGTGTGAG	*	NM:i:0	MD:Z:100	AS:i:100	XS:i:0", sam_header)),
            BamRecord(AlignedSegment.fromstring("chr1_subsampled_simulated_read_3	0	chr1_subsampled	4	60	100M	*	0	0	AAAAAAACAAAACTTGAGGCCTGGCCTTCTGCTCCTCTCCAACCTCCCCTTCTCTGGGCCCAAGCCACCTTGGCTGAGGAGGGGGCGAGGAGGTGTGAGC	*	NM:i:0	MD:Z:100	AS:i:100	XS:i:0", sam_header))
        ]

        self.assertListEqual(actual, expected)




class Test_Bam_get_all_unmapped_records(unittest.TestCase):
    '''
    We could do the same thing (create BAM with zero unmapped records, one and four, etc).
    But now let's try a different approach (mocking + patching)
    '''
    def setUp(self):
        '''
        This method is called before each test
        '''
        # TODO : first show what is a Mock (scripts/mock_exercise.py)

        # instead of creating mapped SAM records, let's just create a mock pretending it is a mapped record
        self.bam_record_mapped = Mock()
        self.bam_record_mapped.is_unmapped.return_value = False

        # instead of creating unmapped SAM records, let's just create a mock pretending it is a inmapped record
        self.bam_record_unmapped = Mock()
        self.bam_record_unmapped.is_unmapped.return_value = True

        # instead of creating BAM files with records, let's just create 3 lists with some mapped and unmapped records
        self.bam_with_4_mapped_records_and_0_unmapped_records = [self.bam_record_mapped] * 4
        self.bam_with_4_mapped_records_and_1_unmapped_record = [self.bam_record_mapped] * 4 + [self.bam_record_unmapped]
        self.bam_with_4_mapped_records_and_3_unmapped_records = [self.bam_record_mapped] * 4 + [self.bam_record_unmapped] * 3


    def test_bam_with_no_unmapped_records___returns_no_records(self):
        # TODO : execute in debug mode
        bam = Bam(Path("does_not_matter")) # TODO : set breakpoint here, add "bam.get_all_records()" to watches and see how it changes

        # let's replace bam.get_all_records() method with a mock to pretend we have a
        # Bam file with 4 mapped records and 0 unmapped records
        bam.get_all_records = Mock(return_value=self.bam_with_4_mapped_records_and_0_unmapped_records)

        actual = bam.get_all_unmapped_records()
        expected = []

        self.assertListEqual(actual, expected)

    def test_bam_with_no_unmapped_records___version_2___returns_no_records(self):
        # We can be even more assertives about how the tested function is
        bam = Bam(Path("does_not_matter"))

        bam.get_all_records = Mock(return_value=self.bam_with_4_mapped_records_and_0_unmapped_records)

        actual = bam.get_all_unmapped_records()
        expected = []

        self.assertListEqual(actual, expected)

        # We can set how many times a mocked method is called
        # This could be useful to ensure the implementation do not overcall an expensive method, for example
        bam.get_all_records.assert_called_once()
        # bam.get_all_records.assert_not_called() # this fails

        # We can also assert if all records in the BAM were tested
        self.assertEqual(self.bam_record_mapped.is_unmapped.call_count, 4)

        # Note: while it can be important to ensure how the tested functions use its dependencies (mocked objects),
        # it is also important to not control the implementation too strictly, otherwise it makes hard to modify


    def test_bam_with_1_unmapped_record___returns_1_record(self):
        bam = Bam(Path("does_not_matter"))
        bam.get_all_records = Mock(return_value=self.bam_with_4_mapped_records_and_1_unmapped_record)

        actual = bam.get_all_unmapped_records()
        expected = [self.bam_record_unmapped]

        self.assertListEqual(actual, expected)

        bam.get_all_records.assert_called_once()
        self.assertEqual(self.bam_record_mapped.is_unmapped.call_count, 4)
        self.assertEqual(self.bam_record_unmapped.is_unmapped.call_count, 1)


    def test_bam_with_3_unmapped_records___returns_3_record(self):
        bam = Bam(Path("does_not_matter"))
        bam.get_all_records = Mock(return_value=self.bam_with_4_mapped_records_and_3_unmapped_records)

        actual = bam.get_all_unmapped_records()
        expected = [self.bam_record_unmapped, self.bam_record_unmapped, self.bam_record_unmapped]

        self.assertListEqual(actual, expected)

        bam.get_all_records.assert_called_once()
        self.assertEqual(self.bam_record_mapped.is_unmapped.call_count, 4)
        self.assertEqual(self.bam_record_unmapped.is_unmapped.call_count, 3)



    # Note how simple these tests are. All we care about is having a Bam file with some mapped and unmapped records.
    # We don't care about any other alignment information, which can be sort of complicated to create.
    # Mocking allows us to run a test with exactly the only stuff we care about, and ensure how the tested method uses the mocks.




# TODO : exercise: test Bam.there_are_no_unmapped_reads() by mocking Bam.get_all_unmapped_records()