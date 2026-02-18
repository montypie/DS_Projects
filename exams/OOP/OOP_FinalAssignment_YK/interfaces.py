from abc import ABC, abstractmethod


class Searchable(ABC):
    """ Defines methods for searchable items """

@abstractmethod
def matches_search(search_term: str) -> bool:
    """ Checks if an item matchtes search_term """
    pass

@abstractmethod
def get_search_keywords() -> list:
    """ Returns list of searchable attributes """
    pass