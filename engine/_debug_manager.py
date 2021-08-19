"""_debug_manager.py contains the DebugManager base class, which is used to
debug the engine.
"""

import os
import signal
from threading import Thread

from flask import Flask, jsonify, request

from ._eobject import EObject

# from ._loggar import Log


class App(Flask):
    """App class is the Flask class that implements the server debugger.
    """

    def __init__(self, the_name):
        """__init__ initializes App instance.
        """
        super().__init__(the_name)
        self.engine = None
        self.server_pid = None

    def run_server(self):
        """run_server launches Flask server.
        """
        self.run(host="0.0.0.0", debug=False, port=5010)

    def api_managers(self):
        """api_managers returns all engine managers.
        """
        a_result = {key: manager.name for key, manager in self.engine.managers.items() if manager is not None}
        return jsonify(a_result)

    def api_exit(self):
        """api_exit exits the engine.
        """
        self.engine.on_exit()
        return jsonify("exiting engine...")

    def api_kill(self):
        """api_kill kills Flask server.
        """
        # print("killing server {}...".format(self.server_pid))
        # os.kill(self.server_pid, signal.SIGKILL)


app = App(__name__)


@app.route("/managers", methods=["GET", ])
def api_managers():
    """app_managers retrieve all engine managers.
    """
    return app.api_managers()


@app.route("/exit", methods=["GET", ])
def api_exit():
    """api_exit exits the engine.
    """
    app.server_pid = os.getpid()
    return app.api_exit()


class DebugManager(EObject):
    """DebugManager class implements the base class for any custom game.
    """

    def __init__(self, the_name, the_engine=None):
        """__init__ initializes the DebugManager instance.

        Args:
            the_name (str): String with the DebugManager name.
            the_engine (Engine): Engine instance.
        """
        super().__init__(the_name, the_engine)
        self.thread = None

    def on_end(self):
        """on_end ends the debug manager.
        """
        app.api_kill()

    def on_init(self):
        """on_init initalizes test debugger and start thread and
        flask app.
        """
        super().on_init()
        app.engine = self.engine
        self.thread = Thread(target=app.run_server, daemon=True)
        self.thread.start()
