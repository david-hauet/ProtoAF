from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import PROTECT

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
        (PLANET_TYPE_WARM_JUPITER, 'Warm Jupiter'),
        (PLANET_TYPE_WARM_NEPTUNE, 'Warm Neptune'),
        (PLANET_TYPE_WARM_SUPER_EARTH, 'Warm Super-Earth'),
        (PLANET_TYPE_WARM_MINI_NEPTUNE, 'Warm Mini-Neptune'),
        (PLANET_TYPE_HOT_JUPITER, 'Hot Jupiter'),
        (PLANET_TYPE_HOT_NEPTUNE, 'Hot Neptune'),
        (PLANET_TYPE_HOT_SUPER_EARTH, 'Hot Super-Earth'),
        (PLANET_TYPE_HOT_MINI_NEPTUNE, 'Hot Mini-Neptune'),
        (PLANET_TYPE_COLD_JUPITER, 'Cold Jupiter'),
        (PLANET_TYPE_COLD_NEPTUNE, 'Cold Neptune'),
        (PLANET_TYPE_COLD_SUPER_EARTH, 'Cold Super-Earth'),
        (PLANET_TYPE_COLD_MINI_NEPTUNE, 'Cold Mini-Neptune'),
        (PLANET_TYPE_UNASSIGNED, 'Unassigned'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=PLANET_TYPE, default=PLANET_TYPE_UNASSIGNED)
    priority = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
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

    #X_moe: Margin of error of variable X
    #Example: parallax_moe is the predicted margin of error for the observed or calculated parallax value.
      
    name = models.CharField(max_length=255)
    ra = models.CharField(max_length=255)
    dec = models.CharField(max_length=255)
    stellar_distance = models.DecimalField(max_digits=13, decimal_places=9, null=True, blank=True)
    parallax = models.DecimalField(max_digits=13, decimal_places=9, null=True, blank=True)
    parallax_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    ecliptic_latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    ecliptic_longiude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    galactic_latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    galactic_longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    
    orbiting_planets = models.ForeignKey(Exoplanet, on_delete=models.PROTECT)

    total_proper_motion = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    total_proper_motion_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    proper_motion_ra = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    proper_motion_ra_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)
    
    proper_motion_dec = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    proper_motion_dec_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)
    
    effective_temperature = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    effective_temperature_moe = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)

    spectral_type = models.CharField(max_length=5, null=True, blank=True)

    metallicity = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    metallicity_moe = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)

    density = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    density_moe = models.DecimalField(max_digits=9, decimal_places=8, null=True, blank=True)

    mass = models.DecimalField(max_digits=9, decimal_places=5, null=True, blank=True)
    mass_moe = models.DecimalField(max_digits=7, decimal_places=5, null=True, blank=True)

    radius = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    radius_moe = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)

    surface_gravity = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    surface_gravity_moe = models.DecimalField(max_digits=9, decimal_places=8, null=True, blank=True)

    luminosity = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    luminosity_moe = models.DecimalField(max_digits=9, decimal_places=8, null=True, blank=True)

    radial_velocity = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    radial_velocity_moe = models.DecimalField(max_digits=16, decimal_places=15, null=True, blank=True)

    age = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    age_moe = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    rotational_velocity = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    rotational_velocity_moe = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    rotation_period = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    rotation_period_moe = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)


    #Photometry
    mV = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mV_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mTESS = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mTESS_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mJ = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mJ_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mH = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mH_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mKS = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mKS_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mW1 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mW1_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mW2 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mW2_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mW3 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mW3_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mW4 = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mW4_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mGAIA = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mGAIA_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    mB = models.DecimalField(max_digits=6, decimal_places=4, null=True, blank=True)
    mB_moe = models.DecimalField(max_digits=10, decimal_places=9, null=True, blank=True)

    

    


class Light_curve (models.Model):
    associated_planet = models.ForeignKey(Exoplanet, on_delete=models.PROTECT)
    image = models.FileField(null=True)


class Synthetic_spectre (models.Model):
    associated_planet = models.ForeignKey(Exoplanet, on_delete=PROTECT)
    image = models.FileField(null=True)


    





