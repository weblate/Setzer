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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CodeFoldingPresenter(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.source_gutter = self.model.document.view.source_view.get_gutter(Gtk.TextWindowType.LEFT)

        self.tag_table = self.model.document.source_buffer.get_tag_table()
        self.line_invisible = dict()

        self.source_gutter.insert(self.view, 3)
        self.view.connect('query-data', self.query_data)
        self.model.register_observer(self)

    def change_notification(self, change_code, notifying_object, parameter):

        if change_code == 'is_enabled_changed':
            if self.model.is_enabled:
                self.show_folding_bar()
            else:
                self.hide_folding_bar()

        if change_code == 'buffer_changed':
            buffer = parameter
            for i in range(len(self.line_invisible), buffer.get_end_iter().get_line() + 1):
                self.line_invisible[i] = False

        if change_code == 'folding_regions_updated':
            self.update_line_visibility()

        if change_code == 'folding_state_changed':
            if parameter['is_folded']:
                self.hide_region(parameter)
            else:
                self.show_region(parameter)

    def show_region(self, region):
        tag = self.get_invisible_region_tag(region['id'])
        source_buffer = self.model.document.source_buffer
        start_iter = source_buffer.get_start_iter()
        end_iter = source_buffer.get_end_iter()
        source_buffer.remove_tag(tag, start_iter, end_iter)
        self.delete_invisible_region_tag(region['id'])
        self.update_line_visibility()

    def hide_region(self, region):
        tag = self.get_invisible_region_tag(region['id'])
        source_buffer = self.model.document.source_buffer
        mark_start = region['mark_start']
        start_iter = source_buffer.get_iter_at_mark(mark_start)
        mark_end = region['mark_end']
        end_iter = source_buffer.get_iter_at_mark(mark_end)
        end_iter.forward_char()
        source_buffer.apply_tag(tag, start_iter, end_iter)
        self.update_line_visibility()

    def get_invisible_region_tag(self, region_id):
        tag = self.tag_table.lookup('invisible_region_' + str(region_id))
        if tag == None:
            tag = self.model.document.source_buffer.create_tag('invisible_region_' + str(region_id), invisible=1)
        return tag

    def delete_invisible_region_tag(self, region_id):
        tag = self.tag_table.lookup('invisible_region_' + str(region_id))
        if tag != None:
            self.tag_table.remove(tag)

    def update_line_visibility(self):
        for i in range(len(self.line_invisible)):
            self.line_invisible[i] = False
        for region in self.model.folding_regions.values():
            if region['is_folded']:
                for line in range(region['starting_line'] + 1, region['ending_line'] + 1):
                    self.line_invisible[line] = True
        self.source_gutter.queue_draw()

    def query_data(self, renderer, start_iter, end_iter, state):
        if self.line_invisible[start_iter.get_line()]: return
        if start_iter.get_line() in self.model.folding_regions.keys():
            if self.model.folding_regions[start_iter.get_line()]['is_folded']:
                renderer.set_icon_name('own-folded-symbolic')
            else:
                renderer.set_icon_name('own-unfolded-symbolic')
        else:
            renderer.set_icon_name('own-no-folding-symbolic')

    def show_folding_bar(self):
        self.view.set_visible(True)

    def hide_folding_bar(self):
        self.view.set_visible(False)


