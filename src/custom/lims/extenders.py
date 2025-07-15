from zope.interface import implements
from zope.component import adapts
from plone.app.content.interfaces import INameFromTitle
# from bika.lims.content.sample import Sample
# from bika.lims.interfaces import ISample
# from bika.lims.interfaces import ISample
# from senaite.lims.content.sample import Sample
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from Products.Archetypes import atapi
from Products.Archetypes.public import AnnotationStorage, AttributeStorage, StringField, StringWidget

from custom.lims.interfaces import ICustomLimsLayer  # your browser layer

from plone.supermodel import model
from zope import schema
# from bika.lims.content.analysisrequest import IAnalysisRequest
from bika.lims.interfaces import IAnalysisRequest
from zope.interface import implementer
from zope.schema.fieldproperty import FieldProperty

from bika.lims.content.analysisrequest import AnalysisRequest

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
    
class ExtraARFields(object):
    implements(ISchemaExtender)
    adapts(IAnalysisRequest)
    # adapts(ISample)

    fields = [
        StringField(
            "wellPosition",
            # storage=AnnotationStorage(),
            storage=AttributeStorage(),
            required=False,
            # mutator="setWellPosition",
            # accessor="getWellPosition",
            widget=StringWidget(
                # label="Well Position",
                visible={'view': 'visible', 'edit': 'visible', 'header_table': 'visible', 'add' : 'edit'},
            ),
        )
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    # Define accessor/mutator methods
    # def getWellposition(self):
    #     return self.context.getField("wellPosition").get(self.context)

    # def setWellposition(self, value):
    #     return self.context.getField("wellPosition").set(self.context, value)
    
    # def getWellPosition(self):
    #     import logging; logging.getLogger().info("Fetching wellPosition")
    #     return self.getField("wellPosition").get(self)


    # def setWellPosition(self, value):
    #     return self.getField("wellPosition").set(self, value)
    
    # def setWellPosition(self, value):
    #     import logging
    #     logging.getLogger().info("Setting wellPosition = %s", value)
    #     return self.getField("wellPosition").set(self, value)

    # AnalysisRequest.getWellPosition = getWellPosition
    # AnalysisRequest.setWellPosition = setWellPosition

