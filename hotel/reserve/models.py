from django.db import models

class Hotel(models.Model):
    how_many_rooms=models.IntegerField(blank=False , null=False)
    name_hotel=models.CharField(max_length=20 , blank=False , null=False)
    special_features=models.CharField(max_length=100 , default='' , blank=True)
    phone_hotel=models.BigIntegerField(blank=False , null=False)
    grade_hotel=models.IntegerField(blank=False , null=False)

    def __str__(self):
        return  self.name_hotel
        return  self.special_features


class place(Hotel):
    name_country=models.CharField(max_length=20, blank=False , null=False)
    name_city=models.CharField(max_length=20 , blank=False , null=False)
    addres_hotel=models.CharField(max_length=20 , blank=False , null=False)

    def __str__(self):
        self.name_city
        self.name_country
        self.addres_hotel


class Room (models.Model):
    hotel=models.ForeignKey(Hotel , on_delete=models.CASCADE)
    room_prices=models.FloatField(blank=False , null=False)
    special_features_room=models.CharField(max_length=100 ,blank=True , null=True)
    room_capacity=models.IntegerField(blank=False , null=False)
    reserved=models.BooleanField(default=False)
    room_number=models.IntegerField(blank=False , null=False)
    room_floor=models.IntegerField(blank=False , null=False)
    garde_room=models.IntegerField(blank=False , null=False)



