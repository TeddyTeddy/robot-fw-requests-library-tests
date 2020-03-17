from LibraryLoader import LibraryLoader
from robot.api.deco import keyword
from robot.api import logger


class AdminUser:
    """
    This Robot Library makes requests to BlogPostAPI as Admin User.
    It contains private methods for CRUD Requests as well as OPTIONS request.
    It exposes keywords to operate on postings
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton
        # read all necessary variables from CommonVariables.py
        self._admin = self._loader.builtin.get_variable_value("${ADMIN}")
        self._session_alias = self._loader.builtin.get_variable_value("${ADMIN_SESSION}")
        self._api_base_url = self._loader.builtin.get_variable_value("${API_BASE_URL}")
        self._postings_uri = self._loader.builtin.get_variable_value("${POSTINGS_URI}")
        self._expected_options_response_headers = self._loader.builtin.get_variable_value("${OPTIONS_RESPONSE_HEADERS}")

        self._loader.rl.create_session(alias=self._session_alias, url=self._api_base_url, cookies={}, verify=True)

    @keyword
    def make_options_request(self):
        return self._loader.rl.options_request(alias=self._session_alias, uri=self._postings_uri,
                                               headers=self._admin['OPTIONS_REQUEST_HEADERS'])
    @keyword
    def verify_options_response(self, options_response):
        assert options_response.status_code == 200
        assert options_response.headers['Allow'] == self._expected_options_response_headers['Allow']
        assert options_response.headers['Vary'] == self._expected_options_response_headers['Vary']
        assert options_response.headers['Content-Type'] == self._expected_options_response_headers['Content-Type']
        assert options_response.json() == self._admin['EXPECTED_API_SPEC']






