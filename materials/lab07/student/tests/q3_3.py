OK_FORMAT = True
test = {   'name': 'q3_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(preban_rates, Table)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> preban_rates.num_rows == 44\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(preban_rates.column("Death Penalty") == True)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(preban_rates.column("Year") == 1971)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(elem in death_penalty.column("State") for elem in preban_rates.column("State"))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
