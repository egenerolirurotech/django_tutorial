from django.db.models import Model, CharField, BooleanField

# Create your models here
class Member(Model):
    firstname: str = CharField(max_length=255)
    lastname: str = CharField(max_length=255)
    is_active: bool = BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} -- active: {self.is_active}"
