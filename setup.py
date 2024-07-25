from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Influence Game API'
LONG_DESCRIPTION = 'A Python API to query and interact with the state of the game Influence'

setup(
    name='influencepy',
    version=VERSION,
    author='Viktor K. Koerner',
    author_email='koerner-axs@protonmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['influence', 'api', 'starknet', 'ethereum', 'blockchain']
)
