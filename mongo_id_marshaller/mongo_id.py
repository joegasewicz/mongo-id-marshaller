from typing import Dict, Any, List, Generator


def _doc_generator(mongo_docs: List[Dict[str, Any]]) -> Generator:
    for doc in mongo_docs:
        yield doc


class MongoId:

    identifier: str = "_id"

    def __init__(self, *, id_key: str = "id"):
        self.id_key = id_key

    def single(self, query_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        :param query_data: Mongo Document
        :return:
        """
        _key = query_data.pop(self.identifier)
        query_data[self.id_key] = str(_key)
        return query_data

    def multiple(self, query_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        :param query_list: List of Mongo Documents
        :return:
        """
        cleaned_list = []
        for query_data in _doc_generator(query_list):
            cleaned_list.append(self.single(query_data))
        return cleaned_list
