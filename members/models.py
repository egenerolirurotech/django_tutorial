from django.db.models import Model, CharField

# Create your models here
class Member(Model):
    firstname: str = CharField(max_length=255)
    lastname: str = CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
