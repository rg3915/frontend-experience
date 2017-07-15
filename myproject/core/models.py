from django.db import models


TREATMENT = (
    ('a', 'Arq.'),
    ('aa', 'Arqa.'),
    ('d', 'Dona'),
    ('dr', 'Dr.'),
    ('dra', 'Dra.'),
    ('e', 'Eng.'),
    ('ea', u'Engª.'),
    ('p', 'Prof.'),
    ('pa', 'Profa.'),
    ('sr', 'Sr.'),
    ('sra', 'Sra.'),
    ('srta', 'Srta.'),
)


class Person(models.Model):
    treatment = models.CharField(
        'tratamento', max_length=4, choices=TREATMENT, null=True, blank=True)
    first_name = models.CharField('nome', max_length=50)
    last_name = models.CharField(
        'sobrenome', max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=20, null=True, blank=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return '%s %s %s' % (self.treatment, self.first_name, self.last_name)
