from typing import Literal


def _configure_as_prod():



def _configure_as_test():
    pass


def configure_environment(environment: Literal['prod', 'test'] = 'test'):
    if environment == 'prod':
        _configure_as_prod()
    elif environment == 'test':
        _configure_as_test()
    else:
        raise ValueError(f'Unknown environment: {environment}')
