# -*- coding: utf-8 -*-

# Copyright (C) 2005 Osmo Salomaa
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

"""Text formatting actions for :class:`gaupol.Application`."""

import aeidon
import gaupol
_ = aeidon.i18n._


class ShowCaseMenuAction(gaupol.MenuAction):

    """Show the case format menu."""

    def __init__(self):
        """Initialize a :class:`ShowCaseMenuAction` instance."""
        gaupol.MenuAction.__init__(self, "show_case_menu")
        self.set_label(_("Ca_se"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


class ToggleDialogDashesAction(gaupol.Action):

    """Add or remove dialogue dashes on the selected texts."""

    def __init__(self):
        """Initialize a :class:`ToggleDialogDashesAction` instance."""
        gaupol.Action.__init__(self, "toggle_dialogue_dashes")
        self.set_label(_("_Dialogue"))
        self.set_tooltip(_("Add or remove dialogue dashes on the selected texts"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


class ToggleItalicizationAction(gaupol.Action):

    """Italicize or unitalicize the selected texts."""

    def __init__(self):
        """Initialize a :class:`ToggleItalicizationAction` instance."""
        gaupol.Action.__init__(self, "toggle_italicization")
        self.set_icon_name("format-text-italic")
        self.set_label(_("_Italic"))
        self.set_tooltip(_("Italicize or unitalicize the selected texts"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))
        doc = page.text_column_to_document(col)
        markup = page.project.get_markup(doc)
        aeidon.util.affirm(markup is not None)
        aeidon.util.affirm(markup.italic_tag is not None)


class UseLowerCaseAction(gaupol.Action):

    """Change the selected texts to lower case."""

    def __init__(self):
        """Initialize a :class:`UseLowerCaseAction` instance."""
        gaupol.Action.__init__(self, "use_lower_case")
        self.set_label(_("_Lower"))
        self.set_tooltip(_("Change the selected texts to lower case"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


class UseSentenceCaseAction(gaupol.Action):

    """Change the selected texts to sentence case."""

    def __init__(self):
        """Initialize a :class:`UseSentenceCaseAction` instance."""
        gaupol.Action.__init__(self, "use_sentence_case")
        self.set_label(_("_Sentence"))
        self.set_tooltip(_("Change the selected texts to sentence case"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


class UseTitleCaseAction(gaupol.Action):

    """Change the selected texts to title case."""

    def __init__(self):
        """Initialize a :class:`UseTitleCaseAction` instance."""
        gaupol.Action.__init__(self, "use_title_case")
        self.set_label(_("_Title"))
        self.set_tooltip(_("Change the selected texts to title case"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


class UseUpperCaseAction(gaupol.Action):

    """Change the selected texts to upper case."""

    def __init__(self):
        """Initialize a :class:`UseUpperCaseAction` instance."""
        gaupol.Action.__init__(self, "use_upper_case")
        self.set_label(_("_Upper"))
        self.set_tooltip(_("Change the selected texts to upper case"))
        self.action_group = "main-unsafe"

    def _affirm_doable(self, application, page, selected_rows):
        """Raise :exc:`aeidon.AffirmationError` if action cannot be done."""
        aeidon.util.affirm(page is not None)
        aeidon.util.affirm(selected_rows)
        col = page.view.get_focus()[1]
        aeidon.util.affirm(col is not None)
        aeidon.util.affirm(page.view.is_text_column(col))


__all__ = tuple(x for x in dir() if x.endswith("Action"))
