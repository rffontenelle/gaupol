# -*- coding: utf-8 -*-

# Copyright (C) 2012 Osmo Salomaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Video actions for :class:`gaupol.Application`."""

import aeidon
import gaupol

class LoadVideoAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "load-video")
        self.accelerators = ["<Control>L"]
        self.action_group = "safe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(gaupol.util.gst_available())
        aeidon.util.affirm(page is not None)

class PlayPauseAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "play-pause")
        self.accelerators = ["P"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)

class PlaySelectionAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "play-selection")
        self.accelerators = ["O"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)
        aeidon.util.affirm(selected_rows)

class SeekBackwardAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-backward")
        self.accelerators = ["<Shift><Ctrl>Left"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)

class SeekForwardAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-forward")
        self.accelerators = ["<Shift><Ctrl>Right"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)

class SeekNextAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-next")
        self.accelerators = ["<Ctrl>Right"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)

class SeekPreviousAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-previous")
        self.accelerators = ["<Ctrl>Left"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)

class SeekSelectionEndAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-selection-end")
        self.accelerators = ["<Ctrl>Down"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)
        aeidon.util.affirm(selected_rows)

class SeekSelectionStartAction(gaupol.Action):
    def __init__(self):
        gaupol.Action.__init__(self, "seek-selection-start")
        self.accelerators = ["<Ctrl>Up"]
        self.action_group = "unsafe"
    def _affirm_doable(self, application, page, selected_rows):
        aeidon.util.affirm(application.player is not None)
        aeidon.util.affirm(selected_rows)

__all__ = tuple(x for x in dir() if x.endswith("Action"))
