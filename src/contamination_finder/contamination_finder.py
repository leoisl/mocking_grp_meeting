from src.bam.bam import Bam
from src.index.index import Index
from collections import Counter
from typing import Optional
from src.contamination_finder.contamination_explanation import Contamination_Explanation, Species_Explanation_Tuple

# TODO : do not show implementation in the overview
class Contamination_Finder:
    def __init__(self, bam: Bam, index: Index, original_species: str):
        self._bam = bam
        self._index = index
        self._original_species = original_species


    # TODO: test with mocks
    def get_species_most_found_in_unmapped_reads(self) -> Optional[str]:
        species_to_frequency = Counter() # e.g. "E. coli": 100, "H. sapiens": 250, etc

        for unmapped_read in self._bam.get_all_unmapped_records():
            unmapped_read_sequence = unmapped_read.get_sequence() # e.g. "ACGTTTCGA"
            species_for_the_given_sequence = self._index.get_species_for_the_given_sequence(unmapped_read_sequence) # e.g. ["E. coli", "E. coli", "S. enterica"]
            for species in species_for_the_given_sequence:
                species_to_frequency[species] += 1 # increase the species' frequency

        # get the most common species and its frequency
        most_common_specie_and_frequency_list = species_to_frequency.most_common(1) # e.g. [("E. coli", 250)]

        we_found_nothing_in_the_index = len(most_common_specie_and_frequency_list) == 0
        if we_found_nothing_in_the_index:
            return None
        else:
            specie = most_common_specie_and_frequency_list[0][0] # e.g. "E. coli"
            return specie


    def get_contamination_report (self) -> Species_Explanation_Tuple:
        if self._bam.there_are_no_unmapped_reads():
            return Species_Explanation_Tuple(species=None,
                                             explanation=Contamination_Explanation.NO_CONTAMINATION_ALL_READS_WERE_MAPPED)

        species = self.get_species_most_found_in_unmapped_reads()
        if species is None:
            return Species_Explanation_Tuple(species=None,
                                             explanation=Contamination_Explanation.CONTAMINATION_UNKNOWN)

        if species == self._original_species:
            return Species_Explanation_Tuple(species=species,
                                             explanation=Contamination_Explanation.NO_CONTAMINATION_BUT_YOUR_REFERENCE_IS_INCOMPLETE)
        else:
            return Species_Explanation_Tuple(species=species,
                                             explanation=Contamination_Explanation.CONTAMINATION_SUCCESFULLY_IDENTIFIED)

