import requests

MAINNET_API_URL = 'https://api.influenceth.io'
PRE_RELEASE_API_URL = 'https://api-prerelease.influenceth.io'


class InfluenceClient:
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 endpoint_url: str = MAINNET_API_URL
                 ):
        """
        Construct an Influence API client, that by default connects to the MAINNET API.

        :param client_id: ID assigned to this app
        :param client_secret: Secret/Token
        :param endpoint_url: URL of the API endpoint
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._endpoint_url = endpoint_url
        self._session = requests.Session()
        self._authorize()

    def _authorize(self):
        req = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        resp = self._session.post(self._endpoint_url + '/v1/auth/token', json=req)
        resp.raise_for_status()
        self._token = resp.json()['access_token']
        self._session.headers['Authorization'] = 'Bearer ' + self._token

    def _get(self, url: str):
        if self._token is None:
            raise Exception('Not authorized')
        if url.startswith('/'):
            url = self._endpoint_url + url
        resp = self._session.get(url)
        resp.raise_for_status()
        return resp.json()

    def get_crew(self, id: int):
        """

        :param id:
        :return:
        """
        crew = self._get(f'/v1/crew/{id}')
        # TODO: implement for real
        return crew

    def get_activities(self,
                       crew_id: int,
                       page_num: int = 1,
                       page_size: int = 25
                       ):
        """

        :param id:
        :return:
        """
        # TODO: add type filtering??
        activities = self._get(f'/v2/entities/{crew_id}/activity?page={page_num}&pageSize={page_size}')
        # TODO: parse activities: see src/api/activity-schema.ts
        return activities

    def get_entities(self,
                     ):
        pass
