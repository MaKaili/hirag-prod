from abc import ABC, abstractmethod
from typing import List

from hirag_prod.schema import Entity, Relation


class BaseGDB(ABC):
    @abstractmethod
    async def upsert_relation(self, relation: Relation):
        raise NotImplementedError

    @abstractmethod
    async def query_one_hop(self, query: str) -> (List[Entity], List[Relation]):
        raise NotImplementedError

    @abstractmethod
    async def query_graph_by_keys(
        self, keys: List[str]
    ) -> (List[Entity], List[Relation]):
        raise NotImplementedError
