import json

DATA_FILE_PATH = '/home/sagivt/PycharmProjects/Vim/code-interview/providers/providers.json'
PROVIDERS = {}


def load_providers():
    global PROVIDERS
    if not PROVIDERS:
        f = open(DATA_FILE_PATH, "r")
        PROVIDERS = json.loads(f.read())
        PROVIDERS = sorted(PROVIDERS, key=lambda k: k['score'], reverse=True)
        f.close()
    return PROVIDERS


def get_providers_by(specialty = '', date = 0, min_score = 0):
    load_providers()
    return [x['name'] for x in PROVIDERS if
            (float(x['score']) >= min_score) and
            (specialty.lower() in map(str.lower, x['specialties'])) and
            len([time for time in x['availableDates'] if
                    int(time['from']) <= date and int(time['to']) >= date]) > 0]


def is_availability_exist(name='', date=0):
    load_providers()
    data = [x for x in PROVIDERS if
            name in x['name'] and
            len([time for time in x['availableDates'] if
                 int(time['from']) <= date <= int(time['to'])]) > 0]

    return len(list(data)) > 0
