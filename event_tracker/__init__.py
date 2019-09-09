"""
Add GamificationProcessor to event tracking backends list.
"""
__version__ = "0.0.1"

from django.conf import settings as django_settings

from event_tracker.settings import EVENT_TRACKING_TRACKING_PROCESSOR


default_app_config = 'gamma_bridge.apps.GamificationTrackingConfig'

django_settings.EVENT_TRACKING_TRACKING_BACKENDS['tracking_logs']['OPTIONS']['processors'] += [
    {'ENGINE': EVENT_TRACKING_TRACKING_PROCESSOR}
]