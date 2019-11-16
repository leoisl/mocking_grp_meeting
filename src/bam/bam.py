from src.bam.bam_record import BamRecord
from pysam import AlignmentFile
from pathlib import Path
from typing import Generator

# TODO: Talk about wrappers/adaptor classes
class Bam:
    def __init__(self, bam_filepath: Path):
        self._bam_filepath = bam_filepath

    def get_all_reads(self) -> Generator[BamRecord, None, None]:
        bam_file = AlignmentFile(self._bam_filepath, "rb")
        for record in bam_file:
            yield BamRecord(record)
        bam_file.close()

    def get_all_unmapped_reads(self) -> Generator[BamRecord, None, None]:
        for record in self.get_all_reads():
            if record.is_unmapped():
                yield record

    def there_are_no_unmapped_reads(self) -> bool:
        return len(list(self.get_all_unmapped_reads())) == 0