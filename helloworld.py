"""Define a simple example plugin."""

# ba_meta require api 6

from __future__ import annotations

from typing import TYPE_CHECKING

import ba

if TYPE_CHECKING:
    pass


# ba_meta export plugin
class MyPlugin(ba.Plugin):
    """My first ballistica plugin!"""

    def on_app_launch(self) -> None:
        ba.screenmessage('HELLO WORLD FROM MYPLUGIN!!!!', color=(0, 1, 0))

