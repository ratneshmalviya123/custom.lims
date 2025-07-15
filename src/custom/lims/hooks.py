# -*- coding: utf-8 -*-
from bika.lims.interfaces import IAnalysisRequest
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zope.component import adapter
from zope.lifecycleevent import modified
import logging

logger = logging.getLogger(__name__)

@adapter(IAnalysisRequest, IObjectModifiedEvent)
def custom_ar_id_generator(ar, event):
    try:
        current_id = ar.getId()
        if current_id and current_id.endswith("Seq03d"):
            return  # Don't overwrite if already set

        client = ar.getClient()
        client_id = client.getClientID() if client else "Unknown"
        date = ar.getSamplingDate()
        date_str = date.strftime("%Y%m%d") if date else "nodate"

        new_id = "{}-{}-Seq03d".format(client_id, date_str)
        ar.setId(new_id)
        logger.info("✅ AR ID set on modification: {}".format(new_id))
    except Exception as e:
        logger.error("❌ Failed to set AR ID: {}".format(e))



@adapter(object, IObjectModifiedEvent)
def custom_sample_id_generator(obj, event):
    # Only handle objects of type "Sample"
    if getattr(obj, "portal_type", "") != "Sample":
        return

    try:
        ar = obj.getAnalysisRequest()
        client = ar.getClient() if ar else None
        client_id = client.getClientID() if client else "Unknown"

        date = ar.getSamplingDate() if ar else None
        date_str = date.strftime("%Y%m%d") if date else "nodate"

        new_id = "{}-{}-Seq03d".format(client_id, date_str)

        if obj.getId() != new_id:
            obj.setId(new_id)
            logger.info("✅ Sample ID set: {}".format(new_id))

    except Exception as e:
        logger.error("❌ Failed to set Sample ID: {}".format(e))

