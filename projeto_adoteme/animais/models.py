from django.db import models

class Usuario(models.Model):
    nome = models.CharField("Insira o nome do usuário: ",
                            max_length=80)

    def __str__(self):
        return self.nome

class Adotante(Usuario):
    cpf = models.CharField("Insira o CPF, somente números, excluindo pontos e hífen: ",
                        max_length=11,
                        unique=True)

class Abrigo(Usuario):
    cnpj = models.CharField("Insira o CNPJ, somente números, excluindos pontos e hífen: ",
                            max_length=14,
                            unique=True)
    
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario,
                                 on_delete=models.CASCADE,
                                 related_name='perfil')
    comprovante_endereco = models.FileField(upload_to='usuarios/comprovantes_enderecos',
                                            blank=True,
                                            null=True)
    bio = models.TextField(blank=True,
                           null=True,
                           max_length=150)
    avatar = models.ImageField(upload_to='usuarios/avatars/',
                               blank=True,
                               null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.nome}"

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