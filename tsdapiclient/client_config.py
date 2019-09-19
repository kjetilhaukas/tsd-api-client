
"""Common tacl internal config."""

API_VERSION = 'v1'
PROD = 'https://api.tsd.usit.no/{0}'.format(API_VERSION)
TEST = 'https://test.api.tsd.usit.no/{0}'.format(API_VERSION)
ENV = {'test': TEST, 'prod': PROD}
