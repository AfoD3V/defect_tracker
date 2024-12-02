from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Project(models.Model):
    project_name = models.TextField()
    created_at = models.TimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.project_name


class UserProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Project: {self.project} -> User: {self.user}"


class Domain(models.Model):
    domain_name = models.TextField()

    def __str__(self):
        return self.domain_name


class Defect(models.Model):

    class Status(models.TextChoices):
        NEW = "N", "New"
        IN_PROGRESS = "IP", "In Progress"
        ANALYSIS = "A", "Analysis"
        REJECTED = "R", "Rejected"
        DONE = "D", "Done"
        REOPENED = "RP", "Re-opened"

    class Priority(models.TextChoices):
        HIGH = "H", "High"
        MEDIUM = "M", "Medium"
        LOW = "L", "Low"

    class Severity(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        CRITICAL = "C", "Critical"

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    summary = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.NEW,
    )
    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    severity = models.CharField(
        max_length=1,
        choices=Severity.choices,
        default=Severity.A,
    )
    steps = models.TextField()
    expected_result = models.TextField()
    actual_result = models.TextField()

    def __str__(self):
        return self.summary


class Comment(models.Model):
    defect = models.ForeignKey(Defect, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text


class Attachment(models.Model):
    file = models.FileField(upload_to="attachments/")
    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    defect = models.ForeignKey(Defect, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.file_name
