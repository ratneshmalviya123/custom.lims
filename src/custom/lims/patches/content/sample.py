# from hoch.lims import check_installed

# @check_installed(None)
def getVolume(self):  # noqa camelcase, but compliant with AT's
    """Returns the volume of the sample in uL.
    """
    return self.getField("Volume").get(self)

def getWellPosition(self):  # noqa camelcase, but compliant with AT's
    """Returns the well position of the sample.
    """
    return self.getField("WellPosition").get(self)