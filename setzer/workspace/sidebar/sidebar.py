#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017, 2018 Robert Griesel
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
# along with this program. If not, see <http://www.gnu.org/licenses/>

import setzer.workspace.sidebar.symbols_page.symbols_page as symbols_page
import setzer.workspace.sidebar.document_structure_page.document_structure_page as document_structure_page
from setzer.app.service_locator import ServiceLocator


class Sidebar(object):

    def __init__(self, workspace):
        self.view = ServiceLocator.get_main_window().sidebar
        self.workspace = workspace

        self.document_structure_page = document_structure_page.DocumentStructurePage(workspace)
        self.view.add_named(self.document_structure_page.view, 'document_structure')

        self.symbols_page = symbols_page.SymbolsPage(workspace)
        self.view.add_named(self.symbols_page.view, 'symbols')

        self.view.queue_draw()


