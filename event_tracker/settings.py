

EVENT_TRACKING_TRACKING_PROCESSOR = 'event_tracker.processor.EventTrackerProcessor'

EVENT_TRACKING_TRACKING_BACKENDS = {
    'logger': {
        'ENGINE': EVENT_TRACKING_TRACKING_PROCESSOR,
        'OPTIONS': {
            'name': 'tracking'
        }
    }
}
