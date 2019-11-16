from typing import List
from abc import ABC, abstractmethod

# Abstract classes: makes you explicitly tell what an Index needs to implement
# Makes your code rely on abstract concepts and interfaces, instead of real implementation
# Other parts of the code don't really care how Indexes are implemented, as long they respect this interface
# TODO: develop better on this
class Index(ABC):
    @abstractmethod
    def get_species_of_perfect_hits_for_the_given_sequence (self, sequence: str) -> List[str]:
        pass