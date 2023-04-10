import requests
import csv
import json

URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="

def load_csv_files_as_dict() -> json:
    """loads people csv as dict"""
    with open('people.csv', newline='') as csv_file:
        return list(csv.DictReader(csv_file))


def get_nearest_court_from_postcode(postcode: list) -> list:
    """Given a postcode get the nearest courts to that postcode"""
    response = requests.get(f"{URL}{postcode}", timeout = 10)
    if response.status_code > 200 and response.status_code < 500:
        raise Exception("Unable to locate matching court.", 404)
    if response.status_code >= 500:
        raise Exception("Unable to connect to server.", 500)
    courts_json = response.json()
    return courts_json

def get_nearest_court_of_same_type(courts_json: list, type: str) -> dict:
    """returns the nearest court of the desired type form the courts json"""
    for court in courts_json:
        if type in court['types']:
            return court


def filter_nearest_court(court_data: dict) -> dict:
    """filters out the necessary data from the nearest court to a person"""
    name = court_data["name"]
    dx_number = court_data["dx_number"]
    distance = court_data["distance"]
    return {"nearest_court": name, "dx_number": dx_number, "distance": distance}


def find_persons_nearest_court_of_desired_type(people):
    """merges nearest court data with csv data"""
    with open('people.json', 'w', newline='') as f:
        for person in people:
            courts_json = get_nearest_court_from_postcode(person['home_postcode'])
            court_data = get_nearest_court_of_same_type(courts_json, person['looking_for_court_type'])
            person.update(filter_nearest_court(court_data))
            json.dump(person, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    people = load_csv_files_as_dict()
    find_persons_nearest_court_of_desired_type(people)

