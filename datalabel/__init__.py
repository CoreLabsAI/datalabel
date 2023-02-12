from .LUI import LabelService

def __init__(self):
    return LabelService()


def label(msgs, tags_list = None, labels = None, classes = None):
    ls = LabelService()
    df = ls.label(msgs, tags_list = None, labels = None, classes = None)
    return df

