from zope.interface import implements
from zope.component import adapts
from plone.app.content.interfaces import INameFromTitle
# from bika.lims.content.sample import Sample
# from bika.lims.interfaces import ISample
# from bika.lims.interfaces import ISample
# from senaite.lims.content.sample import Sample
from archetypes.schemaextender.interfaces import ISchemaModifier
from Products.Archetypes import atapi
from Products.Archetypes.public import AnnotationStorage, AttributeStorage, StringField, StringWidget

from custom.lims.interfaces import ICustomLimsLayer  # your browser layer

from plone.supermodel import model
from zope import schema
from bika.lims.interfaces import IAnalysisRequest
from zope.interface import implementer
from zope.schema.fieldproperty import FieldProperty
from bika.lims.content.analysisrequest import AnalysisRequest    
from zope.interface import implements, implementer
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.Field import StringField, IntegerField, ReferenceField
from Products.Archetypes.Widget import IntegerWidget, StringWidget, ReferenceWidget

class StringExtensionField(ExtensionField, StringField):
    pass

class IntegerExtensionField(ExtensionField, IntegerField):
    pass

class ReferenceExtensionField(ExtensionField, ReferenceField):
    pass


WellPosition = StringExtensionField(
                name="wellPosition",
                # label=u"Well Position", 
                widget=StringWidget(
                    # description=u"Enter Well Position",
                    label=u"Well Position", 
                    visible={'view': 'visible', 
                             'edit': 'visible', 
                             'header_table': 'visible', 
                             'add' : 'edit'},
                    custom_js=(
                        u"jq(document).ready(function() {"
                        u"  setTimeout(function() {"
                        u"    jq('input[name$=wellPosition-0]').attr('placeholder', 'Enter Well Position');"
                        u"  }, 100);"
                        u"});",
                    ),
                ),
                required=False,
            )

PlateID = StringExtensionField(
                name="plateID",
                # label=u"Plate ID ",
                widget=StringWidget(
                    # label=u"\u200B",  # zero-width space (prevents label fallback) 
                    label=u"Plate ID ",
                    description=u"If Plate is submitted, enter Plate ID",
                    visible={'view': 'visible', 
                             'edit': 'visible', 
                             'header_table': 'visible', 
                             'add' : 'edit'},
                    custom_js=(
                        u"jq(document).ready(function() {"
                        u"  setTimeout(function() {"
                        u"    jq('input[name$=plateID-0]').attr('placeholder', 'If Plate is submitted, enter Plate ID');"
                        u"  }, 100);"
                        u"});",
                    ),

                ),
                required=False,
            )

PlateID = StringExtensionField(
    name="plateID",
    widget=StringWidget(
        label=u"Plate ID",
        description=u"",  # leave this blank if using placeholder
        visible={
            'view': 'visible',
            'edit': 'visible',
            'header_table': 'visible',
            'add': 'edit',
        }
    ),
    required=False,
)
@implementer(IOrderableSchemaExtender)
class ExtraARFields(object):
    """Schema extender for the Sample content type."""
    adapts(IAnalysisRequest)
    # implements(ISchemaExtender)
    # layer = ICustomLimsLayer

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas
    
    def getFields(self):
        return [
            WellPosition, 
            PlateID
        ]
        
    # def getWellPosition(self):
    #     import logging; logging.getLogger().info("Fetching wellPosition")
    #     return self.getField("wellPosition").get(self)

    # def setWellPosition(self, value):
    #     return self.getField("wellPosition").set(self, value)
    
    # AnalysisRequest.getWellPosition = getWellPosition
    # AnalysisRequest.setWellPosition = setWellPosition
    
# class ICustomAnalysisRequest(IAnalysisRequest):
#     """Custom schema for Analysis Request"""

#     custom_field = schema.TextLine(
#         title=u"Custom Field",
#         description=u"A custom field added to AR",
#         required=False,
#     )


# @implementer(ICustomAnalysisRequest)
# class CustomAnalysisRequest(AnalysisRequest):
#     """Extended AnalysisRequest class"""
#     # Override methods here if needed
    
#     custom_field = FieldProperty(ICustomAnalysisRequest['custom_field'])

#     def custom_method(self):
#         return "Extended logic"

#     def __init__(self, context):
#         self.context = context

#     def getFields(self):
#         return self.fields
    
