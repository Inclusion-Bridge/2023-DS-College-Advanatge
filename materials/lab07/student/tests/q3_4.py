OK_FORMAT = True
test = {   'name': 'q3_4',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(postban_rates, Table)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> postban_rates.num_rows == 44\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(postban_rates.column("Death Penalty") == False)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all(postban_rates.column("Year") == 1973)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(elem in postban_rates.column("State") for elem in preban_rates.column("State"))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
