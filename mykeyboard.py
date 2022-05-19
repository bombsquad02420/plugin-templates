"""Defines my math keyboard."""

# ba_meta require api 6

from __future__ import annotations

from typing import TYPE_CHECKING

import ba

if TYPE_CHECKING:
    from typing import Tuple, Dict


# ba_meta export keyboard
class MathKeyboard(ba.Keyboard):
    """Math keyboard with some extra symbols."""
    name = 'Math'
    chars = [('+', '-', '*', '=', '&', '_'),
             ('/', '%', '.', '^', '#'),
             ('(', ')', '?', '$')]
    nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '`', '~', '@')
    pages: Dict[str, Tuple[str, ...]] = {}
