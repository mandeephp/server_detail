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
        db_table = 'Date21072024'

    def __str__(self):
        return f"{self.server} - {self.start_time}"