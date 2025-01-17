#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017-present Robert Griesel
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
gi.require_version('PangoCairo', '1.0')
from gi.repository import GObject
from gi.repository import Pango
from gi.repository import PangoCairo
import cairo

import time

from setzer.app.service_locator import ServiceLocator
from setzer.helpers.timer import timer


class WelcomeScreen(object):

    def __init__(self):
        self.view = ServiceLocator.get_main_window().welcome_screen

        self.text = list()
        self.text.append('Reiciendis libero nemo sint autem. Maxime et ea qui provident. Sunt nihil eaque quidem dolores sequi debitis. Temporibus quia ut fuga sint pariatur aut.')
        self.text.append('Autem dolore aut quo in qui. Aut dolor dignissimos laborum eum perspiciatis iusto et veniam. Voluptate ea pariatur omnis qui eum ab est. Sequi ut sint rerum et.')
        self.text.append('Dolore nulla sunt corporis voluptatum dolore reprehenderit. Molestiae est unde sint facere iusto ea impedit. Soluta temporibus mollitia totam id earum. At inventore amet omnis. Dignissimos itaque perspiciatis dolore.')
        self.text.append('Illum et molestias quia provident. Dolores aut quis molestiae cumque. Unde dignissimos placeat possimus. Sit et ullam quia deserunt illo inventore. Id modi quidem fugit fuga magni possimus praesentium.')
        self.text.append('Aliquid commodi qui tempore et. Tempora ullam quod nisi eum dolores voluptatem quia culpa. Provident et voluptate dignissimos aliquam qui aut ratione. Dolorum qui qui nostrum consequatur.')
        self.text.append('Saepe perspiciatis ducimus vitae suscipit eligendi mollitia. Delectus quo praesentium ut sit. Dolor non aliquid maiores enim minus. Exercitationem mollitia quia et atque itaque. Doloremque voluptas esse debitis similique. Repellendus qui doloribus aut ea quod perferendis libero autem.')
        self.text.append('Architecto qui sit quis voluptatem. Est nobis modi deleniti ullam sunt eum quia sed. Expedita asperiores odit dicta quam ut. Ratione qui qui hic quia eligendi sed qui.')
        self.text.append('Natus et eum velit eveniet assumenda delectus nihil. Non eligendi vitae voluptatum nihil omnis ex molestiae. Excepturi velit dignissimos ut quia quae nemo. Maxime laborum in ad repellendus dolore qui repudiandae et. Sed laudantium non nesciunt.')
        self.text.append('Consectetur qui sed autem expedita aut quae aut. Qui et sit sit aliquam consequatur sed esse est. Provident dolorem facere libero voluptas est voluptatem sed.')
        self.text.append('Ullam non esse et ex alias sunt aut. Eaque beatae et veritatis. Est consequatur exercitationem illo repudiandae magni. Qui aspernatur quasi placeat qui veritatis dolores. Assumenda et nobis hic.')
        self.text.append('Reiciendis libero nemo sint autem. Maxime et ea qui provident. Sunt nihil eaque quidem dolores sequi debitis. Temporibus quia ut fuga sint pariatur aut.')
        self.text.append('Autem dolore aut quo in qui. Aut dolor dignissimos laborum eum perspiciatis iusto et veniam. Voluptate ea pariatur omnis qui eum ab est. Sequi ut sint rerum et.')
        self.text.append('Dolore nulla sunt corporis voluptatum dolore reprehenderit. Molestiae est unde sint facere iusto ea impedit. Soluta temporibus mollitia totam id earum. At inventore amet omnis. Dignissimos itaque perspiciatis dolore.')
        self.text.append('Illum et molestias quia provident. Dolores aut quis molestiae cumque. Unde dignissimos placeat possimus. Sit et ullam quia deserunt illo inventore. Id modi quidem fugit fuga magni possimus praesentium.')
        self.text.append('Aliquid commodi qui tempore et. Tempora ullam quod nisi eum dolores voluptatem quia culpa. Provident et voluptate dignissimos aliquam qui aut ratione. Dolorum qui qui nostrum consequatur.')
        self.text.append('Saepe perspiciatis ducimus vitae suscipit eligendi mollitia. Delectus quo praesentium ut sit. Dolor non aliquid maiores enim minus. Exercitationem mollitia quia et atque itaque. Doloremque voluptas esse debitis similique. Repellendus qui doloribus aut ea quod perferendis libero autem.')
        self.text.append('Architecto qui sit quis voluptatem. Est nobis modi deleniti ullam sunt eum quia sed. Expedita asperiores odit dicta quam ut. Ratione qui qui hic quia eligendi sed qui.')
        self.text.append('Natus et eum velit eveniet assumenda delectus nihil. Non eligendi vitae voluptatum nihil omnis ex molestiae. Excepturi velit dignissimos ut quia quae nemo. Maxime laborum in ad repellendus dolore qui repudiandae et. Sed laudantium non nesciunt.')
        self.text.append('Consectetur qui sed autem expedita aut quae aut. Qui et sit sit aliquam consequatur sed esse est. Provident dolorem facere libero voluptas est voluptatem sed.')
        self.text.append('Ullam non esse et ex alias sunt aut. Eaque beatae et veritatis. Est consequatur exercitationem illo repudiandae magni. Qui aspernatur quasi placeat qui veritatis dolores. Assumenda et nobis hic.')
        self.text.append('Reiciendis libero nemo sint autem. Maxime et ea qui provident. Sunt nihil eaque quidem dolores sequi debitis. Temporibus quia ut fuga sint pariatur aut.')
        self.text.append('Autem dolore aut quo in qui. Aut dolor dignissimos laborum eum perspiciatis iusto et veniam. Voluptate ea pariatur omnis qui eum ab est. Sequi ut sint rerum et.')
        self.text.append('Dolore nulla sunt corporis voluptatum dolore reprehenderit. Molestiae est unde sint facere iusto ea impedit. Soluta temporibus mollitia totam id earum. At inventore amet omnis. Dignissimos itaque perspiciatis dolore.')
        self.text.append('Illum et molestias quia provident. Dolores aut quis molestiae cumque. Unde dignissimos placeat possimus. Sit et ullam quia deserunt illo inventore. Id modi quidem fugit fuga magni possimus praesentium.')
        self.text.append('Aliquid commodi qui tempore et. Tempora ullam quod nisi eum dolores voluptatem quia culpa. Provident et voluptate dignissimos aliquam qui aut ratione. Dolorum qui qui nostrum consequatur.')
        self.text.append('Saepe perspiciatis ducimus vitae suscipit eligendi mollitia. Delectus quo praesentium ut sit. Dolor non aliquid maiores enim minus. Exercitationem mollitia quia et atque itaque. Doloremque voluptas esse debitis similique. Repellendus qui doloribus aut ea quod perferendis libero autem.')
        self.text.append('Architecto qui sit quis voluptatem. Est nobis modi deleniti ullam sunt eum quia sed. Expedita asperiores odit dicta quam ut. Ratione qui qui hic quia eligendi sed qui.')
        self.text.append('Natus et eum velit eveniet assumenda delectus nihil. Non eligendi vitae voluptatum nihil omnis ex molestiae. Excepturi velit dignissimos ut quia quae nemo. Maxime laborum in ad repellendus dolore qui repudiandae et. Sed laudantium non nesciunt.')
        self.text.append('Consectetur qui sed autem expedita aut quae aut. Qui et sit sit aliquam consequatur sed esse est. Provident dolorem facere libero voluptas est voluptatem sed.')
        self.text.append('Ullam non esse et ex alias sunt aut. Eaque beatae et veritatis. Est consequatur exercitationem illo repudiandae magni. Qui aspernatur quasi placeat qui veritatis dolores. Assumenda et nobis hic.')

        self.font_desc = Pango.FontDescription.from_string('cmr10')
        self.angle = 0.18
        self.alpha = 0.065
        self.font_size = 36
        self.line_height = 70
        self.font_desc.set_size(self.font_size * Pango.SCALE)

        self.is_active = False
        self.lines_per_second = 0.25
        self.animate = False

        self.fg_color = None
        self.bg_color = None
        self.color_manager = ServiceLocator.get_color_manager()
        self.update_colors()
        self.view.get_style_context().connect('changed', self.update_colors)

        self.view_height = 0
        self.view_width = 0
        self.gradient_size = None
        self.gradient_surface = None
        self.update_gradient()
        self.view.connect('size-allocate', self.update_gradient)

        self.view.drawing_area.connect('draw', self.draw)

    def activate(self):
        self.is_active = True
        self.do_draw()
        if self.animate:
            GObject.timeout_add(15, self.do_draw)

    def deactivate(self):
        self.is_active = False

    def do_draw(self):
        self.view.drawing_area.queue_draw()
        return self.is_active

    @timer
    def draw(self, drawing_area, ctx):
        self.view_width = self.view.get_allocated_width()
        self.view_height = self.view.get_allocated_height()

        ctx.rotate(-self.angle)
        ctx.set_source_rgba(self.fg_color.red, self.fg_color.green, self.fg_color.blue, self.fg_color.alpha)

        layout = Pango.Layout(drawing_area.get_pango_context())
        layout.set_font_description(self.font_desc)

        if self.animate:
            y = -self.line_height - int(time.time() * self.line_height * self.lines_per_second) % self.line_height
            line = int(int(time.time() * self.lines_per_second) % self.lines_per_second) + int(self.lines_per_second * (int(time.time()) % int(20 // self.lines_per_second)))
        else:
            y = -70
            line = 0

        text = self.text[line:] + self.text[:line]
        for paragraph in text:
            ctx.rotate(self.angle)
            y += self.line_height
            ctx.move_to(-50, y)
            ctx.rotate(-self.angle)

            layout.set_text(paragraph)
            PangoCairo.show_layout(ctx, layout)

            if y > (self.view_height + self.view_width / 3): break

        ctx.rotate(self.angle)
        self.draw_gradient(ctx)

    #@timer
    def draw_gradient(self, ctx):
        overlay_width = max(self.view.header.get_allocated_width(), self.view.description.get_allocated_width())

        y = int(self.view_height / 2 - self.gradient_size / 2) - 25
        x_start = int(self.view_width / 2 - overlay_width / 2 - self.gradient_size / 2.5)
        x_end = self.view_width - x_start - self.gradient_size

        ctx.set_source_surface(self.gradient_surface)
        for x in range(x_start, x_end, int((x_end - x_start) / 6)):
            self.gradient_surface.set_device_offset(-x, -y)
            ctx.rectangle(x, y, self.gradient_size, self.gradient_size)
            ctx.fill()

    #@timer
    def update_gradient(self, widget=None, allocation=None):
        self.gradient_size = int(self.view.overlay.get_allocated_height() * 2.5)
        self.gradient_surface = cairo.ImageSurface(cairo.Format.ARGB32, self.gradient_size, self.gradient_size)

        gradient_context = cairo.Context(self.gradient_surface)
        pattern = cairo.RadialGradient(self.gradient_size / 2, self.gradient_size / 2, 0, self.gradient_size / 2, self.gradient_size / 2, self.gradient_size / 2)
        pattern.add_color_stop_rgba(0, self.bg_color.red, self.bg_color.green, self.bg_color.blue, self.bg_color.alpha * 0.9)
        pattern.add_color_stop_rgba(1, self.bg_color.red, self.bg_color.green, self.bg_color.blue, 0)
        gradient_context.set_source(pattern)
        gradient_context.move_to(0, 0)
        gradient_context.line_to(self.gradient_size, 0)
        gradient_context.line_to(self.gradient_size, self.gradient_size)
        gradient_context.line_to(0, self.gradient_size)
        gradient_context.close_path()
        gradient_context.fill()

    def update_colors(self, style_context=None):
        self.fg_color = self.color_manager.get_theme_color_mix('theme_fg_color', 'theme_bg_color', self.alpha)
        self.bg_color = self.color_manager.get_theme_color('theme_bg_color')

        self.do_draw()


