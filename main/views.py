from datetime import date, datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout as logoutuser
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import UserLogin
from .models import Solution, ConnectedSolution, Action , Communal
from django.contrib.auth.hashers import make_password


def utilites(request):
    mounth = request.GET.get('mounth')
    userID = request.GET.get('userID')
   
    if userID and mounth:
        Communal.objects.create(mounth=mounth,author=userID).save()  

    
    users = User.objects.filter(is_superuser=False)
    
    comunals = Communal.objects.all()
    MYcomunals = Communal.objects.filter(author = request.user.pk)
    comunalsList =[]
    MYcomunalsList =[]
    for i in comunals:
        user = User.objects.get(pk=i.author)
        examlpe = {
            'first_name':user.first_name,
            'last_name':user.last_name,
            'adress':user.email,
            'mounth':i.mounth,
            'date':i.date,            
        }
        comunalsList.append(examlpe)
    for i in MYcomunals:
        user = User.objects.get(pk=i.author)
        examlpe = {
            'first_name':user.first_name,
            'last_name':user.last_name,
            'adress':user.email,
            'mounth':i.mounth,
            'date':i.date,            
        }
        MYcomunalsList.append(examlpe)
        
        
        
    data={
        'users':users,
        'comunalsList':comunalsList[::-1],
        'MYcomunalsList':MYcomunalsList[::-1],
    }

    return render(request, 'main/utilites.html',data)


def homeConnect(request):
    connectSolutionID = request.GET.get('connectSolutionID')
    runAction = request.GET.get('runAction')

    if runAction:
        Action.objects.create(solution=runAction,
                              author=request.user.pk).save()

    if connectSolutionID:
        if ConnectedSolution.objects.filter(id=connectSolutionID, status='connected').count() == 0:
            ConnectedSolution.objects.filter(
                id=connectSolutionID).update(status='connected')

    solutions = Solution.objects.all()
    connectSolutions = ConnectedSolution.objects.all()
    solutionList = []
    for i in solutions:
        if connectSolutions.filter(solutionID=i.pk, status='treatment').count() > 0:
            userID = connectSolutions.filter(
                solutionID=i.pk, status='treatment')[0].author
            id = connectSolutions.filter(
                solutionID=i.pk, status='treatment')[0].id

            user = User.objects.get(pk=userID)

            last_name = user.last_name
            first_name = user.first_name
            email = user.email

            example = {
                'id': id,
                'solution': i.solution,
                'action': i.action,
                'date': i.date,
                'author': request.user.pk,
                'adress': email,
                'first_name': first_name+' ',
                'last_name': last_name,
            }
            solutionList.append(example)

    connectedSoltions = ConnectedSolution.objects.filter(status='connected')
    connectedSoltionList = []
    for i in connectedSoltions:
        solution = Solution.objects.get(id=i.solutionID)
        connectedUser = User.objects.get(id=i.author)
        example = {
            'solution': solution.solution,
            'action': solution.action,
            'date': i.date,
            'author': connectedUser.pk,
            'adress': connectedUser.email,
            'first_name': connectedUser.first_name+' ',
            'last_name': connectedUser.last_name,
        }
        connectedSoltionList.append(example)

    selectActionsList = []
    selectActions = ConnectedSolution.objects.filter(
        author=request.user.id, status='connected')
    for i in selectActions:
        selectActionsList.append(Solution.objects.get(pk=i.solutionID))

    data = {
        'solutionList': solutionList,
        'connectedSoltions': connectedSoltionList,
        'selectActionsList': selectActionsList,

    }

    return render(request, 'main/homeConnect.html', data)


def clients(request):
    users = User.objects.filter(is_superuser=False)

    return render(request, 'main/clients.html', {'users': users[::-1]})


def solution(request):
    solution = request.GET.get('solution')
    action = request.GET.get('action')
    homeID = request.GET.get('homeID')

    solutions = Solution.objects.all()
    connectSolutions = ConnectedSolution.objects.all()

    solutionList = []
    for i in solutions:
        if connectSolutions.filter(solutionID=i.pk, author=request.user.pk).count() > 0:
            example = {
                'solution': i.solution,
                'action': i.action,
                'date': i.date,
                'author': request.user.pk,
                'status': connectSolutions.get(solutionID=i.pk, author=request.user.pk).status
            }
            solutionList.append(example)
        else:
            example = {
                'id': i.id,
                'solution': i.solution,
                'action': i.action,
                'date': i.date,
                'author': request.user.pk,
                'status': 'none'
            }
            solutionList.append(example)

    if solution:
        Solution.objects.create(solution=solution, action=action).save()

    if homeID:
        if ConnectedSolution.objects.filter(author=request.user.pk, solutionID=homeID).count() == 0:
            ConnectedSolution.objects.create(
                author=request.user.pk, solutionID=homeID, status='treatment')

    today = datetime.date(datetime.now())
    data = {
        'now': today,
        'solutions': solutionList[::-1],
    }

    return render(request, 'main/solution.html', data)


def dashboard(request):
    users = User.objects.all()
    today = str(date.today())
    yesterday = str(datetime.now() - timedelta(days=1)).split(' ')[0]

    actionsList = []
    actions = Action.objects.all()
    for i in actions:
        userDate = str(i.date).split(' ')[0]
        if userDate == today or userDate == yesterday:
            actionsList.append(i)

    actionsDictonary = []

    for i in actionsList:
        actionAuthor = User.objects.get(pk = i.author)
        actionSolution =  Solution.objects.get(pk=i.solution)
        actionDict = {
            'last_name':actionAuthor.last_name,
            'first_name':actionAuthor.first_name,
            'first_name':actionAuthor.first_name,
            'adress':actionAuthor.email,
            'action':actionSolution.action,
            'date':i.date,            
        }    
        actionsDictonary.append(actionDict)            

    solutions = Solution.objects.all()
    connectSolutions = ConnectedSolution.objects.all()
    solutionList = []
    for i in solutions:
        if connectSolutions.filter(solutionID=i.pk, status='treatment').count() > 0:
            userID = connectSolutions.filter(
                solutionID=i.pk, status='treatment')[0].author
            id = connectSolutions.filter(
                solutionID=i.pk, status='treatment')[0].id

            user = User.objects.get(pk=userID)

            last_name = user.last_name
            first_name = user.first_name
            email = user.email

            example = {
                'id': id,
                'solution': i.solution,
                'action': i.action,
                'date': i.date,
                'author': request.user.pk,
                'adress': email,
                'first_name': first_name+' ',
                'last_name': last_name,
            }
            solutionList.append(example)

    lastUsers = []
    for i in users:
        userDate = str(i.date_joined).split(' ')[0]
        if userDate == today or userDate == yesterday:
            lastUsers.append(i)
    userCount = len(users)
    solutionCount = len(Solution.objects.all())
    connectCount = len(ConnectedSolution.objects.filter(status='connected'))

    connectedSoltions = ConnectedSolution.objects.filter(
        author=request.user.id, status='connected')
    connectedSoltionList = []
    for i in connectedSoltions:
        solution = Solution.objects.get(id=i.solutionID)
        connectedUser = User.objects.get(id=i.author)
        example = {
            'solution': solution.solution,
            'action': solution.action,
            'date': i.date,
            'author': connectedUser.pk,
            'adress': connectedUser.email,
            'first_name': connectedUser.first_name+' ',
            'last_name': connectedUser.last_name,
        }
        connectedSoltionList.append(example)

    if request.user.is_superuser:

        data = {
            'lastusers': lastUsers[::-1],
            'userCount': userCount,
            'solutionCount': solutionCount,
            'solutionList': solutionList,
            'connectCount': connectCount,
            'actionsDictonary': actionsDictonary,
        }
    else:
        data = {
            'lastusers': '',
            'connectedSoltions': connectedSoltionList,
        }

    return render(request, 'main/dashboard.html', data)


def index(request):

    return render(request, 'main/index.html')


def adminRedirect(request):
    return redirect('admin/')


def registration(request):
    username = request.GET.get('username')
    last_name = request.GET.get('last_name')
    first_name = request.GET.get('first_name')
    adress = request.GET.get('adress')
    password1 = request.GET.get('password1')
    password1 = make_password(password1)
    if username:
        if User.objects.filter(username=username).count() == 0:
            user = User.objects.create(username=username, last_name=last_name,
                                       first_name=first_name, email=adress, password=password1,)
            user.save()
            auth_login(request, user)
            return JsonResponse({'errorMessage': 'login'})
        else:
            return JsonResponse({'errorMessage': 'userIsReg'})

    return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
        if form.errors:

            return render(request, 'main/login.html', {'form': form, 'error': True})
    else:
        form = UserLogin()
        if form.errors:

            return render(request, 'main/login.html', {'form': form, 'error': True})
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'main/login.html', {'form': form, })


def logout(request):
    logoutuser(request)
    return redirect('/login')
