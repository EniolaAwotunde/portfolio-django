from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True, help_text="e.g. Travel Technology, Enterprise Platform")
    description = models.TextField(help_text="Short summary shown on project cards")
    role = models.CharField(max_length=200, blank=True, help_text="e.g. Founder & Full-Stack Developer")
    problem = models.TextField(blank=True, help_text="What problem does this solve?")
    solution = models.TextField(blank=True, help_text="How does the project solve it?")
    features = models.TextField(blank=True, help_text="One feature per line")
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated, e.g. React, Node.js, MongoDB")
    challenges = models.TextField(blank=True, help_text="Optional: real challenges faced")
    lessons_learned = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    status = models.CharField(max_length=50, default='Live', help_text="e.g. Live, In Progress")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def feature_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=100, blank=True, help_text="e.g. 'Admin Dashboard'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — {self.caption or 'Untitled'}"


class ContactMessage(models.Model):
    REASON_CHOICES = [
        ('project', 'Project'),
        ('employment', 'Employment'),
        ('collaboration', 'Collaboration'),
        ('general', 'General inquiry'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.CharField(max_length=20, choices=REASON_CHOICES, default='general')
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"