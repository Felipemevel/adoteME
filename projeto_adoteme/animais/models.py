from django.db import models

class CommonInfo(models.Model):
    nome = models.CharField("Insira o nome: ",
                            max_length=50)

    class Meta:
        abstract = True

class TipoAnimal(CommonInfo):

    def __str__(self):
        return self.nome

class Raca(CommonInfo):
    tipo_animal = models.ForeignKey(TipoAnimal,
                                    on_delete=models.CASCADE,
                                    related_name='racas')

    def __str__(self):
        return f"{self.tipo_animal.nome} ({self.nome})"

class Animal(CommonInfo):

    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1,
                            choices=[('M', 'Masculino'),
                                     ('F', 'Feminino')])
    cor = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca,
                             on_delete=models.CASCADE,
                             related_name='animais')
    descricao = models.TextField(blank=True,
                                 null=True)
    disponivel = models.BooleanField(default=True,
                                     null=True)

    def __str__(self):
        return self.nome