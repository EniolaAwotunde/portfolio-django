from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?sent=1#contact')
    else:
        form = ContactForm()

    featured = Project.objects.filter(is_featured=True).first()
    other_projects = Project.objects.exclude(is_featured=True)

    education = [
        {'title': 'MSc Public Health', 'institution': 'University of Chester', 'date': 'Completed January 2023'},
    ]
    certifications = [
        {'title': 'Software Development Training', 'institution': 'GMT Software Academy', 'date': 'Completed May 2026'},
        {'title': 'BCS Foundation Certificate in Business Analysis', 'institution': 'BCS, The Chartered Institute for IT', 'date': ''},
    ]
    experience = [
        {
            'title': 'Founder & Full-Stack Developer',
            'institution': 'FlyFamous',
            'date': 'May 2024 — Present',
            'description': 'Independently designed, built, and launched a full-stack travel-technology platform.',
        },
    ]
    skills = {
        'Frontend': ['React', 'JavaScript', 'TypeScript', 'HTML/CSS', 'Tailwind CSS'],
        'Backend': ['Node.js', 'Express.js', 'Python', 'Django', 'REST API', 'JWT Authentication'],
        'Database': ['MongoDB', 'Mongoose', 'PostgreSQL', 'SQLite'],
        'Tools & Platforms': ['Docker', 'AWS', 'Git', 'GitHub', 'Render', 'CI/CD', 'Stripe'],
    }

    return render(request, 'core/home.html', {
        'featured': featured,
        'other_projects': other_projects,
        'education': education,
        'certifications': certifications,
        'experience': experience,
        'skills': skills,
        'form': form,
        'sent': request.GET.get('sent'),
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})