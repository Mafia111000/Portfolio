from django.shortcuts import render, HttpResponse
from home.models import EditEdu,EditExp,EditProj,EditLin,EditSkill

# Create your views here.
def Home(request):
    skill={}
    exp=[]
    proj=[]
    edu=[]
    for i in EditSkill.objects.all():
        skill[i.Skill]=i.Per
    for i in EditExp.objects.all():
        exp.append([i.Company,i.Designation,i.months,i.Description])   
    for i in EditProj.objects.all():
        proj.append([i.Title,i.Desc,i.Year])
    for i in EditEdu.objects.all():
        edu.append([i.UniName,i.Degree,i.Majors.split(' ')[0],i.Majors.split(' ')[1]])
    ed=edu[::-1]
    e=exp[::-1]
    p=proj[::-1]
    values={'skills':skill,'exp':e,'proj':p,'edu':ed}
    
    return render(request,'home.html',values)
    
def about(request):
    if request.method == 'POST':
        reqq=request.POST.get('id')
        print(reqq)
        if reqq=='0':
            if request.POST.get('pass')=='1379':
                Type=request.POST.get('type')
                if Type == 'Projects':
                    return render(request,'projext.html')
                if Type == 'Work Experience':
                    return render(request,'exp.html')
                if Type == 'Skills':
                    return render(request,'skills.html') 
                if Type == 'Links':
                    return render(request,'links.html')
                if Type == 'Education':
                    return render(request,'edu.html')
            else:
                return render(request,'fuck.html')    
        if reqq=='1':
            ditProj=EditProj(Title=request.POST.get('title'),Desc=request.POST.get('desc'),Year=request.POST.get('year'))
            ditProj.save()
        if reqq=='2':
            ditExp=EditExp(Company=request.POST.get('company'),Description=request.POST.get('desc'),months=request.POST.get('year'), Designation=request.POST.get('desi'))
            ditExp.save()
        if reqq=='3':
            ditSkill=EditSkill(Skill=request.POST.get('skill'),Per=request.POST.get('per'))
            ditSkill.save()
        if reqq=='4':
            ditLin=EditLin(SiteNam=request.POST.get('siteN'),Urlo=request.POST.get('url'))
            ditLin.save()
        if reqq=='5':
            print(request.POST.get('uni'),request.POST.get('degree'),request.POST.get('majors'))
            ditEdu=EditEdu(UniName=request.POST.get('uni'),Degree=request.POST.get('degree'),Majors=request.POST.get('majors'))
            ditEdu.save()
        return render(request,'about.html')
        
    return render(request,'about.html')