# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from custom.lims.testing import CUSTOM_LIMS_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that custom.lims is properly installed."""

    layer = CUSTOM_LIMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if custom.lims is installed."""
        self.assertTrue(self.installer.is_product_installed("custom.lims"))

    def test_browserlayer(self):
        """Test that ICustomLimsLayer is registered."""
        from custom.lims.interfaces import ICustomLims
        from plone.browserlayer import utils

        self.assertIn(ICustomLims, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CUSTOM_LIMS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("custom.lims")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if custom.lims is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("custom.lims"))

    def test_browserlayer_removed(self):
        """Test that ICustomLimsLayer is removed."""
        from custom.lims.interfaces import ICustomLims
        from plone.browserlayer import utils

        self.assertNotIn(ICustomLims, utils.registered_layers())
