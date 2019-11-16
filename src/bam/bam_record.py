from pysam import AlignedSegment

# TODO: Talk about wrappers/adaptor classes
class BamRecord:
    def __init__(self, record: AlignedSegment):
        self._record = record

    def is_unmapped(self) -> bool:
        return self._record.is_unmapped

    def get_sequence(self) -> str:
        return self._record.seq