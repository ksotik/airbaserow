import requests
from baserow.client import BaserowClient, Filter
import typing as t


class AirBaserow:
    _api_url = "https://baserow.io"
    _baserow_client = None

    def __init__(self, base_id: str, table_name: str, api_key: str) -> None:
        self._database_id = base_id
        self._table_id = table_name
        self._token = api_key

    def _init_baserow_client(self):
        if not self._baserow_client:
            self._baserow_client = BaserowClient(self._api_url, token=self._token)

    @property
    def api_url(self) -> t.Optional[str]:
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str) -> None:
        self._api_url = api_url
        self._baserow_client = None

    def get_all(
            self,
            max_records: t.Optional[int] = 100,
            view: t.Optional[str] = None,
            fields: t.Optional[str] = None,
            sort: t.Optional[t.List[str]] = None,
            formula: t.Optional[str] = None
    ) -> ():
        self._init_baserow_client()
        rows = self._baserow_client.list_database_table_rows(table_id=self._table_id,
                                                             order_by=sort,
                                                             size=max_records)
        return rows
