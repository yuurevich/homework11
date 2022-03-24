import json


def data():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        salam = json.load(file)
        return salam


data = data()


def load_candidates_from_json():
    result = []
    for candidate in data:
        result.append(candidate['name'])
    return result


def get_candidate(candidate_id):
    return data[int(candidate_id)-1]


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill):
    return [candidate for candidate in data if skill.lower() in candidate['skills'].lower().split(', ')]



