from django.db import models

class kategori(models.Model):
    tenggara = models.CharField(max_length=100)
    barat = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.tenggara}"

class negara(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    asia = models.CharField(max_length=100)
    eropa = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.asia}"


    


