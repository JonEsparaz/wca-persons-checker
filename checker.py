from typing import List
import csv
import requests
import sys
import urllib
import webbrowser

def check_person(registrant: dict) -> None:
    '''
    Searches for a given name on the WCA website, opens the search page in the browser
    if results found (i.e., the person may exist in the WCA DB).
    '''
    name = registrant.get('Name')
    country = registrant.get('Country')
    name_url_encoded = urllib.parse.quote(name)
    search_url = f'https://www.worldcubeassociation.org/search?q={name_url_encoded}'
    response = requests.get(search_url)

    if 'No people found' in response.text:
        print(f'✅ INFO: No users found for "{name}" ({country}).')
    else:
        print(f'⚠️ WARN: User(s) found for "{name}" ({country}).')
        print('Opening search results in browser...')
        webbrowser.open(search_url)

def get_registrants_with_no_wca_id(filename: str) -> List[dict]:
    '''Returns a list of registrants with no WCA ID from a CSV file.'''
    with open(filename, 'r') as csv_file:
        registrations = list(csv.DictReader(csv_file))
        not_has_wca_id = lambda r: not r['WCA ID']
        return list(filter(not_has_wca_id, registrations))

def print_help_and_exit():
    print('Usage: python checker.py <your_file.csv>')
    sys.exit()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('❌ ERROR: Missing CSV file parameter.')
        print_help_and_exit()

    if sys.argv[1] in ['help', '--help', 'h', '-h']:
        print_help_and_exit()

    for person in get_registrants_with_no_wca_id(sys.argv[1]):
        check_person(person)