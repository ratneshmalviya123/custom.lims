# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.PATIENT.
#
# SENAITE.PATIENT is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2020-2025 by it's authors.
# Some rights reserved, see README and LICENSE.

import six

from AccessControl import ClassSecurityInfo
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.Field import ObjectField
# from senaite.core.api import dtime
# from senaite.patient import api as patient_api
# from senaite.patient.browser.widgets import AgeDoBWidget
from senaite.patient.browser.widgets import FullnameWidget
# from senaite.patient.browser.widgets import TemporaryIdentifierWidget
# from senaite.patient.config import AUTO_ID_MARKER
# from senaite.patient.config import PATIENT_CATALOG
# from senaite.patient.interfaces import IAgeDateOfBirthField
from zope.interface import implementer


# class FullnameField(ExtensionField, ObjectField):
#     """Stores a fullname with four components:
#     firstname, middlename, first_lastname, second_lastname
#     """
#     _properties = ObjectField._properties.copy()
#     _properties.update({
#         "type": "extendedfullname",
#         "default": None,
#         "widget": FullnameWidget,  # Customize or reuse existing
#     })

#     def set(self, instance, value, **kwargs):
#         val = dict.fromkeys(
#             ["firstname", "middlename", "first_lastname", "second_lastname"],
#             ""
#         )

#         if isinstance(value, str):
#             val["firstname"] = value

#         elif value is not None:
#             try:
#                 for key, v in value.items():
#                     if key in val:
#                         val[key] = v
#             except AttributeError:
#                 raise ValueError(f"Type not supported: {type(value)}")

#         if not any(filter(None, val.values())):
#             val = self.getDefault(instance)

#         super(FullnameField, self).set(instance, val, **kwargs)

#     def get_firstname(self, instance):
#         return self.get(instance).get("firstname", "")

#     def get_middlename(self, instance):
#         return self.get(instance).get("middlename", "")

#     def get_first_lastname(self, instance):
#         return self.get(instance).get("first_lastname", "")

#     def get_second_lastname(self, instance):
#         return self.get(instance).get("second_lastname", "")

#     def get_fullname(self, instance):
#         return " ".join(filter(None, [
#             self.get_firstname(instance),
#             self.get_middlename(instance),
#             self.get_first_lastname(instance),
#             self.get_second_lastname(instance),
#         ]))
