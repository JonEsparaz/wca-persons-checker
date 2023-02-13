from typing import List
import csv
import requests
import sys
import urllib
import webbrowser

def check_person(name: str) -> None:
    '''
    Searches for a given name on the WCA website, opens the search page in the browser
    if results found (i.e., the person may exist in the WCA DB).
    '''
    name_url_encoded = urllib.parse.quote(name)
    search_url = f'https://www.worldcubeassociation.org/search?q={name_url_encoded}'
    response = requests.get(search_url)

    if 'No people found' in response.text:
        print(f'✅ INFO: No users found for "{name}"')
    else:
        print(f'❌ WARN: User(s) found for "{name}".')
        print('Opening search results in browser...')
        webbrowser.open(search_url)

def get_names_of_registrants_with_no_wca_id() -> List[str]:
    '''Returns a list of registrants (names) with no WCA ID from a CSV file.'''

    if len(sys.argv) < 2:
        print('ERROR: missing CSV file parameter')
        print_help_and_exit()

    if sys.argv[1] in ['help', '--help', 'h', '-h']:
        print_help_and_exit()
    
    with open(sys.argv[1], 'r') as csv_file:
        registrations = list(csv.DictReader(csv_file))
        not_has_wca_id = lambda r: not r['WCA ID']
        get_name = lambda r: r['Name']
        return list(map(get_name, filter(not_has_wca_id, registrations)))

def print_help_and_exit():
    print('Usage: python checker.py <your_file.csv>')
    sys.exit()

if __name__ == '__main__':
    for name in get_names_of_registrants_with_no_wca_id():
        check_person(name)