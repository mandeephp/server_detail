from django.db import models


class ORMS(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'ORMS'

    def __str__(self):
        return self.name

class ServerMetric(models.Model):

    server = models.CharField(max_length=50, db_column='Server')
    start_time = models.TimeField(db_column='StartTime')
    orms = models.ForeignKey(ORMS, on_delete=models.SET_NULL, null=True)
    m2m = models.IntegerField(db_column='M2M')
    realised = models.IntegerField(db_column='Realised')
    cepos = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='CEPOs')
    pepos = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='PEPOs')
    equity = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='Equity')
    fut_pos = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='FutPos')
    total_pos = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='TotalPos')
    delta = models.DecimalField(decimal_places=3, max_digits= 20, null=True, blank=True, db_column='Delta')
    scripts = models.IntegerField( null=True, blank=True, db_column='Scripts')
    streams = models.IntegerField(null=True, blank=True, db_column='Streams')
    stream_number = models.IntegerField(null=True, blank=True, db_column='StreamNumber')

    class Meta:
        db_table = 'server_metrics'

    def __str__(self):
        return f"{self.server} - {self.start_time}"


class Setup(models.Model):
    MOSL_CHOICES = [
        ('MOSL', 'MOSL'),
        ('DB', 'DB'),
        ('grd', 'GRD'),
        ('gvt', 'GVT'),
        ('master', 'MASTER'),
    ]
    server_dropdown = models.CharField(max_length=50, choices=MOSL_CHOICES, db_column='Setup')
    server = models.CharField(max_length=50, null=True, blank=True, db_column='Server')
    start_time = models.DateTimeField(db_column='StartTime', null=True, blank=True)
    expiry_date = models.DateTimeField(db_column='ExpiryDate', null=True, blank=True)
    ats = models.BooleanField(default=False, db_column="ATS")
    no_of_fold_logged_in = models.CharField(max_length=50, null=True, blank=True, db_column='NoOfFOldLoggedIn')
    order_fired = models.CharField(max_length=50, null=True, blank=True, db_column='OrderFired')
    trades = models.CharField(max_length=50, null=True, blank=True, db_column='Trades')
    dc_trades = models.CharField(max_length=50, null=True, blank=True, db_column='DCTrades')
    scripts_loaded = models.CharField(max_length=50, null=True, blank=True, db_column='ScriptsLoaded')
    contract_file_date = models.DateField(null=True, blank=True, db_column='ContractFileDate')
    stream_id_file_date = models.DateField(null=True, blank=True, db_column='StreamIDFileDate')
    fcast = models.CharField(max_length=100, null=True, blank=True, db_column='Fcast')
    highest_temperature = models.CharField(max_length=50, null=True, blank=True, db_column='HighestTemperature')
    recovery = models.CharField(max_length=50, null=True, blank=True, db_column='Recovery')
    rms_used_margin = models.CharField(max_length=50, null=True, blank=True, db_column='RMSusedmargin')
    stream_id1_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID1_Lastsequence')
    stream_id1_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID1_Livesequence')
    stream_id2_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID2_Lastsequence')
    stream_id2_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID2_Livesequence')
    stream_id3_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID3_Lastsequence')
    stream_id3_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID3_Livesequence')
    stream_id4_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID4_Lastsequence')
    stream_id4_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID4_Livesequence')
    stream_id5_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID5_Lastsequence')
    stream_id5_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID5_Livesequence')
    stream_id6_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID6_Lastsequence')
    stream_id6_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID6_Livesequence')
    stream_id7_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID7_Lastsequence')
    stream_id7_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID7_Livesequence')
    stream_id8_lastsequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID8_Lastsequence')
    stream_id8_livesequence = models.CharField(max_length=50, null=True, blank=True, db_column='StreamID8_Livesequence')

    class Meta:
        verbose_name_plural = 'Setup'
        managed = False
        abstract = True

    @classmethod
    def for_table(cls, table_name):
        return type(f'Setup_{table_name}', (cls,), {
            '__module__': cls.__module__,
            'Meta': type('Meta', (), {
                'db_table': table_name,
                'managed': False
            })
        })

    def __str__(self):
        return self.server