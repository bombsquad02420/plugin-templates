"""Define a simple example game."""

# ba_meta require api 6

from __future__ import annotations

from typing import TYPE_CHECKING

import ba
from bastd.game.deathmatch import DeathMatchGame

if TYPE_CHECKING:
    pass


# ba_meta export game
class MyGame(DeathMatchGame):
    """My first ballistica game!"""

    name = 'My Game!'

    def on_begin(self) -> None:
        super().on_begin()
        ba.screenmessage('HELLO WORLD!!!!', color=(0, 1, 0))
