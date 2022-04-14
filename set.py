from typing import Dict, List


class StringSet:
    def __init__(self, *args: str) -> None:
        self._set: Dict[str, str] = dict()
        self._append_args(*args)

    def _append_args(self, *args: str) -> None:
        for arg in args:
            try:
                self._set[arg[0]] = list(self._set[arg[0]])
            except KeyError:
                self._set[arg[0]] = list()
            self._set[arg[0]].append(arg)

    def add_string(self, string: str) -> None:
        self._set.append(string)

    def query(self, string: str) -> List[str]:
        query = list()
        first_letter = string[0]

        for set_value in self._set[first_letter]:
            if set_value.startswith(string):
                query.append(set_value)

        return query
