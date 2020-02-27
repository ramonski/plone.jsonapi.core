# -*- coding: utf-8 -*-

from browser import decorators
from browser import router

import logging
import version


logger = logging.getLogger("plone.jsonapi.routes")


def initialize(context):
    """ Initializer called when used as a Zope 2 product.
    """
    logger.info("### PLONE.JSONAPI.CORE INITIALIZE ###")

    # Make pyflakes happy
    version
    router
    decorators
