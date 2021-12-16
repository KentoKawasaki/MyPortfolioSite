from django.shortcuts import render

from .models import Profile, Skill, Work
# Create your views here.
def index(request):
    profile = Profile.objects.get(name='Kento')
    context = {
        'profile': profile,
    }
    return render(request, 'portfolio/index.html', context)


def skills(request):
    skills = Skill.objects.all()
    works = Work.objects.all().order_by('-published')[:3] # 公開日を降順に並べ直してデータを取得。ハイフン無しだと昇順
    context = {
        'skills': skills,
        'works': works,
    }
    return render(request, 'portfolio/skills.html', context)


def works(request):
    works = Work.objects.all().order_by('-published')
    context = {
        'works': works,
    }
    return render(request, 'portfolio/works.html', context)
