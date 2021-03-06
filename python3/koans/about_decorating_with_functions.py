#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutDecoratingWithFunctions(Koan):
    def addcowbell(fn):
        print("in addcowbell")
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        print("in mediocre")
        return "o/~ We all live in a broken submarine o/~"

    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(), "o/~ We all live in a broken submarine o/~")
        self.assertEqual(__, self.mediocre_song.wow_factor)

    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        self.assertEqual(__, self.render_tag('llama'))
