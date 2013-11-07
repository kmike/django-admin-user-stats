# -*- coding: utf-8 -*-
from datetime import timedelta
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
try:
    from django.utils.timezone import now
except ImportError:
    from datetime import datetime
    now = datetime.now

from qsstats import QuerySetStats
from admin_tools.dashboard import modules


class BaseChart(modules.DashboardModule):
    """
    Dashboard module with user registration charts.

    With default values it is suited best for 2-column dashboard layouts.
    """
    title = _('Registration chart')
    template = 'admin_user_stats/modules/chart.html'
    chart_size = "580x100"
    days = None
    values_count = 30
    interval = 'days'
    queryset = None
    date_field = 'date_joined'
    aggregate = Count('id')

    def is_empty(self):
        return False

    def __init__(self, *args, **kwargs):
        super(BaseChart, self).__init__(*args, **kwargs)

        if self.days is None:
            self.days = {'days': self.values_count, 'weeks': self.values_count*7, 'months': self.values_count*30, 'years': self.values_count*365}[self.interval]

        self.data = self.get_data(self.interval, self.days)
        self.prepare_template_data(self.data)

    def get_caption(self, dt):
        return {
            'days': dt.day,
            'months': dt.strftime("%b"),
            'weeks': dt.strftime('%W'),
            'years': dt.strftime('%Y'),
        }[self.interval]

    # @cached(60*5)
    def get_data(self, interval, days):
        """ Returns an array with new users count per interval """
        stats = QuerySetStats(self.queryset, self.date_field, aggregate = self.aggregate)
        today = now()
        begin = today - timedelta(days=days-1)
        return stats.time_series(begin, today+timedelta(days=1), interval)

    def prepare_template_data(self, data):
        """ Prepares data for template (it is passed as module attributes) """
        self.captions = [self.get_caption(t[0]) for t in data]
        self.values = [t[1] for t in data]
        self.max_value = max(self.values)



class BaseCharts(modules.Group):
    """ Group module with 3 default registration charts """
    title = _('New Users')
    chart_model = BaseChart

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('children', self.get_charts())
        super(BaseCharts, self).__init__(*args, **kwargs)

    def get_charts(self):
        """ Returns 3 basic chart modules (per-day, per-week and per-month) """
        return [
            self.chart_model(_('By Day'), interval='days'),
            self.chart_model(_('By Week'), interval='weeks'),
            self.chart_model(_('By Month'), interval='months'),
            self.chart_model(_('By Year'), interval='years'),
        ]
