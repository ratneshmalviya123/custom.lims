# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import custom.lims


class CustomLimsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=custom.lims)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "custom.lims:default")


CUSTOM_LIMS_FIXTURE = CustomLimsLayer()


CUSTOM_LIMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CUSTOM_LIMS_FIXTURE,),
    name="CustomLimsLayer:IntegrationTesting",
)


CUSTOM_LIMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CUSTOM_LIMS_FIXTURE,),
    name="CustomLimsLayer:FunctionalTesting",
)
