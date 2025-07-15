# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory


_ = MessageFactory("custom.lims")

from . import extenders

def initialize(context):
    # This is the old-school Zope 2 init hook
    import custom.lims.hooks
