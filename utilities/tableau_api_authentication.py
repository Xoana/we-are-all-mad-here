'''
Get Tableau bearer token using the Tableau API.
Requires yaml (or json) file in the following format:
tableau:
  token_name: <token_name>
  token_secret: <token_secret>
  auth_url: <url_for_authentication>
'''
import json
import click
import requests
from general_utils import get_config


def get_bearer_token(credentials):
    ''' Get bearer token from Tableau API. '''
    tableau_token=credentials['tableau']['token_name']
    tableau_secret=credentials['tableau']['token_secret']
    tableau_auth_url = credentials['tableau']['auth_url']
    
    auth_url = tableau_auth_url

    auth_payload = {
        'credentials': {
            'personalAccessTokenName': tableau_token,
            'personalAccessTokenSecret': tableau_secret,
            'site': {
                'contentUrl': ''
            }
        }
    }

    auth_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', auth_url, headers=auth_headers, data=json.dumps(auth_payload))
    json_response = response.json()

    bearer_token = json_response['credentials']['token']
    site_id = json_response['credentials']['site']['id']

    return bearer_token, site_id


@click.command()
@click.option('--credentials_file', default='.credentials.yaml', show_default=True,
              help='Path to the file in which credentials are stored.')
def main(credentials_file):
    credentials = get_config(credentials_file)

    bearer_token, site_id = get_bearer_token(credentials)    
    print(bearer_token, site_id)


if __name__ == '__main__':
    main()
