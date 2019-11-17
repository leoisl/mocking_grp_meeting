from enum import Enum
from collections import namedtuple

class Contamination_Explanation(Enum):
    NO_CONTAMINATION_ALL_READS_WERE_MAPPED = "No contamination in the dataset, " \
                                             "all your reads were mapped to the reference."
    NO_CONTAMINATION_BUT_YOUR_REFERENCE_IS_INCOMPLETE = "No contamination in the dataset, " \
                                                        "the species most found in the unmapped reads was " \
                                                        "the original specie. Your reference is probably incomplete."
    CONTAMINATION_UNKNOWN = "There is contamination in your dataset, but we don't know which species"
    CONTAMINATION_SUCCESFULLY_IDENTIFIED = "There is contamination in your dataset, and we identified the species."

Species_Explanation_Tuple = namedtuple("Species_Explanation", ["species", "explanation"])