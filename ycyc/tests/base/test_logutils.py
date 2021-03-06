#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase
import sys

import six

from ycyc.base import logutils

if six.PY2:
    import thread as threading
else:
    import threading


class TestLoggerInfo(TestCase):

    def test_usage(self):
        frames = sys._current_frames()
        frame = frames[threading.get_ident()]
        loginfo = logutils.LoggerInfo()

        self.assertIs(frame, loginfo.frame)
        line_based = 25
        self.assertEqual(line_based + 1, loginfo.line_no)
        self.assertEqual(line_based + 2, loginfo.line_no)
        self_func = self.test_usage
        self.assertEqual(self_func.__name__, loginfo.code_name)
