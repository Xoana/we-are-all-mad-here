'''
Get Tableau bearer token using the Tableau API.
Requires yaml (or json) file in the following format:
tableau:
  token_name: <token_name>
  token_secret: <token_secret>
  base_url: <base_api_url>
'''
import json
import click
import requests
from general_utils import get_config



def query_sites(tableau_base_url, bearer_token):
    ''' Query Tableau sites. '''
    sites_url = f'{tableau_base_url}/sites'

    payload={}
    headers = {
    'Authorization': f'Bearer {bearer_token}'
    }

    response = requests.request("GET", sites_url, headers=headers, data=payload)

    print(response.text)

def get_bearer_token(tableau_token,tableau_secret,tableau_base_url):
    ''' Get bearer token from Tableau API. '''
    
    auth_url = f'{tableau_base_url}/auth/signin'

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
    tableau_token=credentials['tableau']['token_name']
    tableau_secret=credentials['tableau']['token_secret']
    tableau_base_url = credentials['tableau']['base_url']

    bearer_token, site_id = get_bearer_token(tableau_token,tableau_secret,tableau_base_url)    
    print(bearer_token, site_id)
    query_sites(tableau_base_url, bearer_token)


if __name__ == '__main__':
    main()
