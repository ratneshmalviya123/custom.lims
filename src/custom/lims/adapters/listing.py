from bika.lims import api
from bika.lims.utils import get_link
from plone.memoize.instance import memoize
from plone.memoize.view import memoize as viewcache
from senaite.app.listing.interfaces import IListingView
from senaite.app.listing.interfaces import IListingViewAdapter
from senaite.app.listing.utils import add_column
from senaite.app.listing.utils import add_review_state
from senaite.manufacture import messageFactory as _
from senaite.manufacture import check_installed
from zope.component import adapts
from zope.component import getMultiAdapter
from zope.interface import implements


# Columns to add
ADD_COLUMNS = [
    ("WellPosition ", {
        "title": _("Well Position"),
        "sortable": True,
    }),
]


class SamplesListingViewAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        # Add new column for all available states
        states = map(lambda r: r["id"], self.listing.review_states)
        add_column(
            listing=self.listing,
            column_id="WellPosition",
            column_values={
                "title": "My new column",
                "sortable": False,
            },
            review_states=states)

    def folder_item(self, obj, item, index):
        item["WellPosition"] = api.get_object(obj).getWellPosition()
        return item
    




# @property
# @memoize
# def senaite_theme(self):
#     return getMultiAdapter(
#         (self.context, self.listing.request),
#         name="senaite_theme")

# def icon_tag(self, name, **kwargs):
#     return self.senaite_theme.icon_tag(name, **kwargs)

# def folder_item(self, obj, item, index):

# batch_batch_size = api.get_object(obj).getBatchSize()
# batch_ReleasedQuantity = api.get_object(obj).getReleasedQuantity()
# item["BatchSize"] = batch_batch_size
# item["ReleasedQuantity"] = batch_ReleasedQuantity

# well_position = api.get_object(obj).getWellPosition()
# item["WellPosition"] = well_position

# sample = api.get_object(obj)
# item["WellPosition"] = obj.getField("wellPosition").get(sample) or "Empty value"

# return item



# def before_render(self):
#     # Additional columns
#     rv_keys = map(lambda r: r["id"], self.listing.review_states)
#     for column_id, column_values in ADD_COLUMNS:
#         add_column(
#             listing=self.listing,
#             column_id=column_id,
#             column_values=column_values,
#             after=column_values.get("after", None),
#             review_states=rv_keys)
        
#     review_states = [self.listing.review_states[0]]
#     for review_state in review_states:
#         review_state.update({"columns": self.listing.columns.keys()})
        
# def before_render(self):
# Add a new filter status
# draft_status = {
#     "id": "draft",
#     "title": "Draft",
#     "contentFilter": {
#         "review_state": "sample_draft",
#         "sort_on": "created",
#         "sort_order": "descending",
#     },
#     "columns": self.listing.columns.keys(),
# }
# self.listing.review_states.append(draft_status)

# Add the column
# self.listing.columns["WellPosition"] = {
#     "title": "Well Position",
#     "sortable": False,
#     "toggle": True,
# }

# Make the new column visible for all filter statuses
# for filter in self.listing.review_states:
#     filter.update({"columns": self.listing.columns.keys()})
            
            

# @implementer(IListingViewAdapter)
# class CustomSampleListingAdapter(object):
#     def __init__(self, view, context):
#         self.view = view
#         self.context = context

#     def folder_columns(self):
#         columns = self.view.folder_columns()
#         columns["Well Position"] = {
#             "title": "Well Position",
#             "index": "getWellPosition",
#             "toggle": True,
#         }
#         return columns

#     def folderitems(self, items):
#         for item in items:
#             obj = item.get("obj")
#             if not obj:
#                 continue
#             item["Well Position"] = getattr(obj, "getWellPosition", lambda: "")()
#         return items
