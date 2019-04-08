ATTR_DEVICE_DATE_TIME = 'device_date_time'
ATTR_RADON_LEVEL = 'radon_level'
DEVICE_CLASS_RADON='radon'
DEVICE_CLASS_ACCELEROMETER='accelerometer'
ILLUMINANCE_LUX = 'lx'
PERCENT = '%'
SPEED_METRIC_UNITS = 'm/s2'
VOLUME_BECQUEREL = 'Bq/m3'
VOLUME_PICOCURIE = 'pCi/L'

BQ_TO_PCI_MULTIPLIER = 0.037

"""
0 - 49 Bq/m3  (0 - 1.3 pCi/L):
No action necessary.
"""
VERY_LOW = [0, 49, 'very low']

"""50 - 99 Bq/m3 (1.4 - 2.6 pCi/L):
Experiment with ventilation and sealing cracks to reduce levels."""
LOW = [50, 99, 'low']

"""100 Bq/m3 - 299 Bq/m3 (2.7 - 8 pCi/L):
Keep measuring. If levels are maintained for more than 3 months,
contact a professional radon mitigator."""
MODERATE = [100, 299, 'moderate']

"""300 Bq/m3 (8.1 pCi/L) and up:
Keep measuring. If levels are maintained for more than 1 month,
contact a professional radon mitigator."""
HIGH = [300, None, 'high']
