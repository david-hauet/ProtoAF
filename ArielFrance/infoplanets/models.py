from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import DecimalField

class Exoplanet (models.Model):

    PLANET_TYPE_WARM_JUPITER = 'WJ'
    PLANET_TYPE_WARM_NEPTUNE = 'WN'
    PLANET_TYPE_WARM_SUPER_EARTH = 'WSE'
    PLANET_TYPE_WARM_MINI_NEPTUNE = 'WMN'
    PLANET_TYPE_HOT_JUPITER = 'HJ'
    PLANET_TYPE_HOT_NEPTUNE = 'HN'
    PLANET_TYPE_HOT_SUPER_EARTH = 'HSE'
    PLANET_TYPE_HOT_MINI_NEPTUNE = 'HMN'
    PLANET_TYPE_COLD_JUPITER = 'CJ'
    PLANET_TYPE_COLD_NEPTUNE = 'CN'
    PLANET_TYPE_COLD_SUPER_EARTH = 'CSE'
    PLANET_TYPE_COLD_MINI_NEPTUNE = 'CMN'
    PLANET_TYPE_UNASSIGNED = 'U'

    PLANET_TYPE = [
        ('PLANET_TYPE_WARM_JUPITER', 'Warm Jupiter'),
        ('PLANET_TYPE_WARM_NEPTUNE', 'Warm Neptune'),
        ('PLANET_TYPE_WARM_SUPER_EARTH', 'Warm Super-Earth'),
        ('PLANET_TYPE_WARM_MINI_NEPTUNE', 'Warm Mini-Neptune'),
        ('PLANET_TYPE_HOT_JUPITER', 'Hot Jupiter'),
        ('PLANET_TYPE_HOT_NEPTUNE', 'Hot Neptune'),
        ('PLANET_TYPE_HOT_SUPER_EARTH', 'Hot Super-Earth'),
        ('PLANET_TYPE_HOT_MINI_NEPTUNE', 'Hot Mini-Neptune'),
        ('PLANET_TYPE_COLD_JUPITER', 'Cold Jupiter'),
        ('PLANET_TYPE_COLD_NEPTUNE', 'Cold Neptune'),
        ('PLANET_TYPE_COLD_SUPER_EARTH', 'Cold Super-Earth'),
        ('PLANET_TYPE_COLD_MINI_NEPTUNE', 'Cold Mini-Neptune'),
        ('PLANET_TYPE_UNASSIGNED', 'Unassigned'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=PLANET_TYPE, default=PLANET_TYPE_UNASSIGNED)
    priority = models.PositiveSmallIntegerField(max_length=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    total_observations = models.PositiveSmallIntegerField(default=0, null=True)
    recent_observations = models.PositiveSmallIntegerField(default=0, null=True)
    ra_j2000 = models.CharField(max_length=255, null=True, blank=True)
    dec_j2000 = models.CharField(max_length=255, null=True, blank=True)
    v_mag = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    r_mag = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    gaia_g_mag = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    depth_mmag = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    transit_duration_hours = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    ephemeris_mid_time_bjd_tdb = models.DecimalField(max_digits=14, decimal_places=6, null=True, blank=True)
    ephemeris_mid_time_uncertainty = models.DecimalField(max_digits=8, decimal_places=7, null=True, blank=True)
    ephemeris_period_days = models.DecimalField(max_digits=13, decimal_places=9, null=True, blank=True)
    ephemeris_period_uncertainty = models.DecimalField(max_digits=8, decimal_places=7, null=True, blank=True)
    ephemeris_current_oc_min = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)

class Star (models.Model):
    name = models.CharField(max_length=255)
    





