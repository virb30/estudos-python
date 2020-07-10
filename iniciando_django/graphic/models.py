from django.db import models

# Create your models here.


class Bomba(models.Model):
    cod_bomba = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=30)
    n_estagio = models.CharField(max_length=8)

    class Meta:
        db_table = "bomba"


class Motor(models.Model):
    cod_motor = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=30)
    potencia = models.FloatField()
    tensao = models.CharField(max_length=15)
    n_fase = models.IntegerField()

    class Meta:
        db_table = "motor"


class Curva(models.Model):
    cod_curva = models.IntegerField(primary_key=True)
    n_curva = models.CharField(max_length=10)
    vazao_min = models.FloatField()
    vazao_max = models.FloatField()

    class Meta:
        db_table = "curva"


class PontoCurva(models.Model):
    cod_curva = models.ForeignKey(Curva, on_delete=models.CASCADE)
    vazao = models.FloatField()
    altura = models.FloatField()
    npsh = models.FloatField()
    rend = models.FloatField()

    class Meta:
        db_table = "ponto_curva"


class Acoplamento(models.Model):
    cod_bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    cod_motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    cod_curva = models.ForeignKey(Curva, on_delete=models.CASCADE)

    class Meta:
        db_table = "acoplamento"
