from src.index.index import Index
from src.index.implementation.bigsi_index import BigsiIndex
from src.index.implementation.cobs_index import CobsIndex
from src.index.implementation.reindeer_index import ReindeerIndex

# Factory class: abstracts the creation of an object
# You don't need to worry how to create an Index, all the logic to create an Index goes here
# If you want to change the Index, you just change the create_an_index() method
# TODO : develop better on this

# With the interface and the factory, we don't really need to look at the implementation of the BigsiIndex, or any other index
# We know they respect our Index interface, and that is all that matters
# Implementation is abstracted by the Abstract Base Class
class IndexFactory:
    @staticmethod
    def create_index() -> Index:
        return IndexFactory._create_BIGSI_index()

    @staticmethod
    def _create_BIGSI_index() -> Index:
        return BigsiIndex("http://api.bigsi.io")

    @staticmethod
    def _create_Cobs_index() -> Index:
        return CobsIndex()

    @staticmethod
    def _create_Reindeer_index() -> Index:
        return ReindeerIndex()
