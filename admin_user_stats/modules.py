# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from base_modules import BaseChart, BaseCharts
from django.utils.translation import ugettext_lazy as _


class RegistrationChart(BaseChart):
    """
    Dashboard module with user registration charts.

    With default values it is suited best for 2-column dashboard layouts.
    """
    title = _('Registration chart')
    template = 'admin_user_stats/modules/chart.html'
    chart_size = "580x100"
    days = None
    interval = 'days'
    queryset = User.objects.filter(is_active=True)
    date_field = 'date_joined'


class RegistrationCharts(BaseCharts):
    """ Group module with 3 default registration charts """
    title = _('New Users')
    chart_model = RegistrationChart

