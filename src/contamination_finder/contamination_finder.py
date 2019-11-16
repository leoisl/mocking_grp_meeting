from src.bam.bam import Bam
from src.index.index import Index
from collections import Counter
from typing import Optional
from src.contamination_finder.contamination_explanation import Contamination_Explanation, Species_Explanation_Tuple

class Contamination_Finder:
    # constructor without dependency injection
    # def __init__(self, bam_filepath: str):
    #     self.bam = Bam(bam_filepath)
    #     self.index = IndexFactory.create_index()

    # constructor with dependency injection
    def __init__(self, bam: Bam, index: Index, original_species: str):
        self._bam = bam
        self._index = index
        self._original_species = original_species



    def get_contamination_report (self) -> Species_Explanation_Tuple:
        if self._bam.there_are_no_unmapped_reads():
            return Species_Explanation_Tuple(species=None,
                                             explanation=Contamination_Explanation.NO_CONTAMINATION_ALL_READS_WERE_MAPPED)

        species = self._get_species_most_found_in_unmapped_reads()
        if species is None:
            return Species_Explanation_Tuple(species=None,
                                             explanation=Contamination_Explanation.CONTAMINATION_UNKNOWN)

        if species == self._original_species:
            return Species_Explanation_Tuple(species=species,
                                             explanation=Contamination_Explanation.NO_CONTAMINATION_BUT_YOUR_REFERENCE_IS_INCOMPLETE)
        else:
            return Species_Explanation_Tuple(species=species,
                                             explanation=Contamination_Explanation.CONTAMINATION_SUCCESFULLY_IDENTIFIED)



    def _get_species_most_found_in_unmapped_reads(self) -> Optional[str]:
        specie_to_frequency = Counter()
        for unmapped_read in self._bam.get_all_unmapped_reads():
            unmapped_read_sequence = unmapped_read.get_sequence()
            species_of_perfect_hits_for_the_given_sequence = self._index.\
                get_species_of_perfect_hits_for_the_given_sequence(unmapped_read_sequence)
            for species in species_of_perfect_hits_for_the_given_sequence:
                specie_to_frequency[species] += 1

        most_common_specie_and_number_of_reads_list = specie_to_frequency.most_common(1)

        if len(most_common_specie_and_number_of_reads_list) == 0:
            return None
        else:
            specie = most_common_specie_and_number_of_reads_list[0][0]
            return specie
