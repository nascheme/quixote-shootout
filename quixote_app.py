import os
import sqlite3
from quixote.publish import Publisher
from quixote import enable_ptl
enable_ptl()
import ui

_DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'hello.db')

def create_publisher():
    db = sqlite3.connect(_DB_PATH)
    return Publisher(ui.RootDirectory(db),
                     display_exceptions='plain')


if __name__ == '__main__':
    from quixote.server.scgi_server import run
    host = 'localhost'
    port = 3000
    print 'creating demo listening on %s:%d' % (host, port)
    run(create_publisher, host=host, port=port)
