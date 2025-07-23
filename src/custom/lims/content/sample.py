from zope.component import adapts

from custom.lims.interfaces import ICustomLims  # your browser layer
from custom.lims import messageFactory as _

from bika.lims.interfaces import IAnalysisRequest
from DateTime import DateTime
# from bika.lims.browser.widgets import DateWidget
from bika.lims.browser.widgets import DateTimeWidget, SelectionWidget
from senaite.core.browser.fields.datetime import DateTimeField
# from bika.lims.browser.fields import DateExtensionField
from zope.interface import implements, implementer
from zope.component import adapts
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.Field import StringField, IntegerField, ReferenceField, DateTimeField
from Products.Archetypes.Widget import IntegerWidget, StringWidget, ReferenceWidget, DateWidget
from Products.Archetypes.public import  StringField, StringWidget
from Products.Archetypes.atapi import FileField
from Products.Archetypes.atapi import FileWidget
# from Products.Archetypes.public import SelectionField, SelectionWidget

# from custom.lims.content.fields import FullnameField
# from custom.lims.browser.widgets.fullname import FullnameWidget

class StringExtensionField(ExtensionField, StringField):
    pass

class IntegerExtensionField(ExtensionField, IntegerField):
    pass
class DateExtensionField(ExtensionField, DateTimeField):
    pass
class ReferenceExtensionField(ExtensionField, ReferenceField):
    pass

@implementer(IOrderableSchemaExtender)
class SampleSchemaExtender(object):
    """Schema extender for the Sample content type."""
    adapts(IAnalysisRequest)
    implements(ISchemaExtender)
    # layer = ICustomLims

    fields = [
        StringExtensionField(
            "PlateID",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Plate ID "),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("If Plate is submitted, enter Plate ID"),
                render_own_label=True,
            )),
        StringExtensionField(
            "WellPosition",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Well Position"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Well position for this sample"),
                render_own_label=True,
            )),
        StringExtensionField(
            "SampleType2",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Sample Type "),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Where the sample came from"),
                render_own_label=True,
            )),
        StringExtensionField(
            "StorageBuffer",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Storage Buffer "),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Where the sample was stored"),
                render_own_label=True,
            )),
        StringExtensionField(
            "Species",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Species "),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Species of the sample"),
                render_own_label=True,
            )),
        StringExtensionField(
            "Volume",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Volume(uL)"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Volume sent in the sample"),
                render_own_label=True,
            )),
        StringExtensionField(
            "Concentration",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Concentration"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                # description=_("Concentration"),
                render_own_label=True,
            )),
        StringExtensionField(
            "Amount",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Amount "),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_("Amount of the sample"),
                render_own_label=True,
            )),
        StringExtensionField(
            "OrderingPhysician",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Ordering Physician"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_(""),
                render_own_label=True,
            )),
        StringExtensionField(
            'PatientIDType',
            mode="rw",
            # read_permission=View,
            # write_permission=FieldEditSampler,
            vocabulary=["Patient ID", "National ID", "Passport ID", "Driver ID", "Votor ID"],
            widget=SelectionWidget(
                format='select',
                label=_("Type of Patient ID"),
                description=_(""),
                # see SamplingWOrkflowWidgetVisibility
                visible={
                    'add': 'edit',
                    'header_table': 'prominent',
                },
                render_own_label=True,
                ),
            ),
        StringExtensionField(
            "PatientIDNumber",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("ID# of Patient"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                description=_(""),
                render_own_label=True,
            )),
        StringExtensionField(
            "PatientFirstName",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("First Name of Patient"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                # placeholder=_("FirstName"),
                render_own_label=True,
            )),
        StringExtensionField(
            "PatientMiddleName",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Middle Name of Patient"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                # placeholder=_("MiddleName"),
                render_own_label=True,
            )),
        StringExtensionField(
            "PatientFirstLastName",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("First Last Name of Patient"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                # placeholder=_("FirstLastName"),
                render_own_label=True,
            )),
        StringExtensionField(
            "PatientSecondLastName",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=StringWidget(
                label=_("Second Last Name of Patient"),
                visible={
                    "add": "edit",
                    "edit": "visible", 
                    "header_table": "visible", 
                },
                # placeholder=_("SecondLastName"),
                render_own_label=True,
            )),
            FileField(
            'SampleQCImage',
            widget=FileWidget(
                label=_("Sample QC Image"),
                description=_("Add one or more images to describe the quality of the sample"),
                render_own_label=True,
                visible={
                    'view': 'invisible',
                    'add': 'edit',
                    'header_table': 'invisible',
                },
                )
            ),
        # FullnameField(
        #     "PatientFullName",
        #     required=True,
        #     # read_permission=View,
        #     # write_permission=FieldEditFullName,
        #     widget=FullnameWidget(
        #         label=_("Patient name"),
        #         entry_mode="parts",
        #         view_format="%(firstname)s %(middlename)s %(lastname)s %(second_lastname)s",
        #         render_own_label=True,
        #         visible={
        #             "add": "edit",
        #             "edit": "visible", 
        #             "header_table": "visible", 
        #         }
        #     )
        # ),
        StringExtensionField(
            'ShippingCompany',
            mode="rw",
            # read_permission=View,
            # write_permission=FieldEditSampler,
            vocabulary=["UPS", "FedEx", "DHL", "Any Other"],
            widget=SelectionWidget(
                format='select',
                label=_("Name of the Shipping Company"),
                description=_(""),
                # see SamplingWOrkflowWidgetVisibility
                visible={
                    'add': 'edit',
                    'edit': 'visible',
                    'header_table': 'prominent',
                },
                render_own_label=True,
                ),
            ),
        StringExtensionField(
        "TrackNumber",
        mode="rw",
        # read_permission=View,
        # write_permission=EditExtendedField,
        widget=StringWidget(
            label=_("Tracking Number Inbound"),
            visible={
                "add": "edit",
                "edit": "visible", 
                "header_table": "visible", 
            },
            description=_(""),
            render_own_label=True,
        )),
        DateExtensionField(
            "ShipmentDate",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=DateTimeWidget(
                label=_("Shipment Date"),
                show_time=False,
                visible={
                    "add": "edit",
                    # "edit": "visible",
                    'secondary': 'disabled',
                    "header_table": "prominent"
                },
                render_own_label=True,
                description=_("Date the sample was shipped or picked up."),
            ),
            default=DateTime(),  # Optional: sets the default to current date/time
            max=DateTime().Date()
        ),
        DateExtensionField(
            "ReceivedDate",
            mode="rw",
            # read_permission=View,
            # write_permission=EditExtendedField,
            widget=DateTimeWidget(
                label=_("Received Date"),
                show_time=False,
                visible={
                    "add": "edit",
                    # "edit": "visible",
                    'secondary': 'disabled',
                    "header_table": "prominent"
                },
                render_own_label=True,
                description=_("Date the sample was received."),
            ),
            default=DateTime(),  # Optional: sets the default to current date/time
            max=DateTime().Date()
        ),
        FileField(
        'ImageOnReceipt',
        widget=FileWidget(
            label=_("Image on Receipt of Sample "),
            description=_("Add one or more images to describe how the samples were received"),
            render_own_label=True,
            visible={
                'view': 'invisible',
                'add': 'edit',
                'header_table': 'invisible',
            },
            )
        ),
        StringExtensionField(
        "ReceivedConditions",
        mode="rw",
        # read_permission=View,
        # write_permission=EditExtendedField,
        widget=StringWidget(
            label=_("Received Conditions"),
            visible={
                "add": "edit",
                "edit": "visible", 
                "header_table": "visible", 
            },
            description=_(""),
            render_own_label=True,
        )),
        StringExtensionField(
        "Workflow",
        mode="rw",
        # read_permission=View,
        # write_permission=EditExtendedField,
        widget=StringWidget(
            label=_("Workflow"),
            visible={
                "add": "edit",
                "edit": "visible", 
                "header_table": "visible", 
            },
            description=_(""),
            render_own_label=True,
        ))
    ]
    
    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas
    
    def getFields(self):
        return self.fields

        
class SampleSchemaModifier(object):
    """Modify Sample Schema Fields
    """
    # layer = 
    implements(ISchemaModifier)
        # IBrowserLayerAwareExtender)
    adapts(IAnalysisRequest)

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        # Modify the original schema as needed
        # schema['Client'].required = False
        # schema['Contact'].required = False

        # schema['SampleType'].required = True
        schema['ClientSampleID'].required = True
        schema['SampleType'].widget.label = _("Sample Origin")
        schema['SampleType'].widget.description = _("Where the sample was collected from")
        schema['DateSampled'].widget.show_time = False
        schema['SamplingDate'].widget.label = _("Expected Delivery of Results")
        # profiles = schema.get("Profiles")
        # profiles.required = True

        return schema
    
def getCurrentDate(instance):
    return DateTime().Date()  # Just the date part
