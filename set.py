from typing import List


class StringSet:
    def __init__(self, *args: str) -> None:
        self._set: List[str] = list(args)

    def add_string(self, string: str) -> None:
        self._set.append(string)

    def query(self, string: str) -> List[str]:
        query = list()

        for set_value in self._set:
            if set_value.startswith(string):
                query.append(set_value)

        return query
