# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from qsstats import QuerySetStats
from admin_tools.dashboard import modules


class RegistrationChart(modules.DashboardModule):
    """
    Dashboard module with user registration charts.

    With default values it is suited best for 2-column dashboard layouts.
    """
    title = _('Registration chart')
    template = 'admin_user_stats/modules/chart.html'
    chart_size = "580x100"
    days = None
    interval = 'days'

    def is_empty(self):
        return False

    def __init__(self, *args, **kwargs):
        super(RegistrationChart, self).__init__(*args, **kwargs)

        if self.days is None:
            self.days = {'days': 30, 'weeks': 30*7, 'months': 30*12}[self.interval]

        self.data = self.get_registrations(self.interval, self.days)
        self.prepare_template_data(self.data)

    def get_caption(self, dt):
        return {
            'days': dt.day,
            'months': dt.strftime("%b"),
            'weeks': dt.strftime('%W'),
        }[self.interval]

    # @cached(60*5)
    def get_registrations(self, interval, days):
        """ Returns an array with new users count per interval """
        stats = QuerySetStats(User.objects.filter(is_active=True), 'date_joined')
        today = datetime.today()
        begin = today - timedelta(days=days-1)
        return stats.time_series(begin, today+timedelta(days=1), interval)

    def prepare_template_data(self, data):
        """ Prepares data for template (it is passed as module attributes) """
        self.captions = [self.get_caption(t[0]) for t in data]
        self.values = [t[1] for t in data]
        self.max_value = max(self.values)

def get_registration_charts():
    """ Returns 3 basic chart modules (per-day, per-week and per-month) """
    return [
        RegistrationChart(_('By Day'), interval='days'),
        RegistrationChart(_('By Week'), interval='weeks'),
        RegistrationChart(_('By Month'), interval='months'),
    ]

class RegistrationCharts(modules.Group):
    """ Group module with 3 default registration charts """
    title = _('New Users')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('children', get_registration_charts())
        super(RegistrationCharts, self).__init__(*args, **kwargs)
