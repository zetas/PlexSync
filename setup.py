
from setuptools import setup, find_packages
from plexsync.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='plexsync',
    version=VERSION,
    description='Sync libraries from multiple Plex servers.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='David Della Vecchia',
    author_email='ddv@qubitlogic.net',
    url='https://github.com/zetas/PlexSync/',
    license='GNU GPLv3',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'plexsync': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        plexsync = plexsync.main:main
    """,
)
