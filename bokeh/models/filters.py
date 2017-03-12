from __future__ import absolute_import

from ..core.properties import Bool, Int, Seq, String
from ..model import Model

class Filter(Model):
    ''' A Filter model represents a row-wise subset of data contained in a ColumnDataSource.

    '''

    filter = Seq(Int, default=[])

class GroupFilter(Filter):
    ''' A GroupFilter represents the rows of a ColumnDataSource where the values of the categorical
    column column_name match the group variable.
    '''

    column_name = String()

    group = String()