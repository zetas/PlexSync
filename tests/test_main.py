
from plexsync.main import PlexSyncTest

def test_plexsync(tmp):
    with PlexSyncTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with PlexSyncTest(argv=argv) as app:
        app.run()
