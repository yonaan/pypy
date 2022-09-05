from django.db import models
from django.forms import CharField
from numpy import true_divide
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance


class MasterSensor(models.Model):
    sensor_id=models.CharField(max_length=20,null=False,blank=False,primary_key=True)
    sensor_description=models.CharField(max_length=50,null=True,blank=True)
    created_by=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=50)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tb_m_sensor'
    
    def __str__(self):
        return self.sensor_id

class MasterThreshold(models.Model):
    sensor_id=models.ForeignKey(MasterSensor,null=False,blank=False,on_delete=models.CASCADE)
    threshold_description=models.CharField(max_length=50,null=True,blank=True)
    threshold_id=models.CharField(max_length=50)
    sensor_warning=models.FloatField()  
    sensor_danger=models.FloatField()
    created_by=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=50)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='tb_m_sensor_threshold'

class Temperature_Data(models.Model):
    sensor_id=models.ForeignKey(MasterSensor,blank=True,null=True,on_delete=models.CASCADE)
    threshold_id=models.ForeignKey(MasterThreshold,blank=True,null=True,on_delete=models.CASCADE)
    device_id=CharField(max_length=50)
    device_name=CharField(max_length=50)
    def sensor_warning(self):
        return self.threshold_id.sensor_warning 
    def sensor_danger(self):
        return self.threshold_id.sensor_danger
    temperature=models.FloatField(null=True, blank=True)
    # status=models.CharField(max_length=20, null=True,blank=True)
    created_by=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='tb_r_sensor'
    
    #def __str__(self):
    #    return self.sensor_id

class Temperature_Trend(models.Model):
    temperature=models.FloatField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='tb_temperatur'
