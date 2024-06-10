from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True, default='Unknown')
    branch = models.CharField(max_length=100, default='Unknown')  # Set default value for branch

    def __str__(self):
        return self.user.username

class Compartment(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_empty = models.BooleanField(default=True)
    student = models.OneToOneField(Student, null=True, blank=True, on_delete=models.SET_NULL)
    otp_expiration = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Compartment {self.number}"

class OTP(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    generated_at = models.DateTimeField()  # Add this field

    def save(self, *args, **kwargs):
        if not self.generated_at:
            self.generated_at = timezone.now()  # Set the generated time
        super().save(*args, **kwargs)

    def __str__(self):
        return f"OTP for {self.student.user.username} - {self.code}"
