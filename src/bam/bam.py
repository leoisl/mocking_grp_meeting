from src.bam.bam_record import BamRecord
from pysam import AlignmentFile
from pathlib import Path
from typing import List

class Bam:
    def __init__(self, bam_filepath: Path):
        self._bam_filepath = bam_filepath

    def get_all_records(self) -> List[BamRecord]:
        bam_file = AlignmentFile(self._bam_filepath, "rb")

        all_records = []
        for record in bam_file:
            all_records.append(BamRecord(record))

        bam_file.close()
        return all_records

    def get_all_unmapped_records(self) -> List[BamRecord]:
        all_records = self.get_all_records()

        unmapped_records = []
        for record in all_records:
            if record.is_unmapped():
                unmapped_records.append(record)

        return unmapped_records

    def there_are_no_unmapped_reads(self) -> bool:
        return len(self.get_all_unmapped_records()) == 0