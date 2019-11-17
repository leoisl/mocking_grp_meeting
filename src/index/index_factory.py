from src.index.index import Index
from src.index.implementation.bigsi_index import BigsiIndex
from src.index.implementation.cobs_index import CobsIndex
from src.index.implementation.reindeer_index import ReindeerIndex

# Factory class: abstracts the creation of an object
# You don't need to worry how to create an Index, all the logic to create an Index goes here
# If you want to change the Index, you just change the create_an_index() method

class IndexFactory:
    @staticmethod
    def create_index() -> Index:
        return IndexFactory.__create_BIGSI_index()

    @staticmethod
    def __create_BIGSI_index() -> Index:
        return BigsiIndex("http://api.bigsi.io")

    @staticmethod
    def __create_Cobs_index() -> Index:
        return CobsIndex()

    @staticmethod
    def __create_Reindeer_index() -> Index:
        return ReindeerIndex()
