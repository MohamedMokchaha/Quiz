from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Account, Question
import json


@csrf_exempt
def manageaccount(request, pk=None):
    if request.method == 'GET':
        # Si l'ID est fourni, récupérer le compte spécifique
        if pk:
            account = Account.objects.filter(id=pk).values('id', 'username', 'email', 'password', 'is_superuser')
            if account.exists():
                return JsonResponse(list(account)[0])
            else:
                return JsonResponse({'error': 'Account not found'}, status=404)
            # Sinon, récupérer tous les comptes
        else:
            accounts = Account.objects.all().values('id', 'username', 'email', 'password', 'is_superuser')
            accounts_list = []
            for account in accounts:
                accounts_list.append(account)
            return JsonResponse(accounts_list, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Vérifier que toutes les données requises sont présentes
            if 'username' in data and 'email' in data and 'password' in data and 'is_superuser' in data:
                account = Account.objects.create(
                    username=data['username'],
                    email=data['email'],
                    password=data['password'],
                    is_superuser=data['is_superuser']
                )
                return JsonResponse({'id': account.id, 'username': account.username, 'email': account.email,
                                     'is_superuser': account.is_superuser}, status=201)
            else:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')

    elif request.method == 'PUT':
        # Assurez-vous qu'un ID est fourni
        if not pk:
            return HttpResponseBadRequest('Account ID is required for PUT request')
        try:
            data = json.loads(request.body)
            account = Account.objects.filter(id=pk).first()
            if account:
                # Mettre à jour les champs fournis
                if 'username' in data:
                    account.username = data['username']
                if 'email' in data:
                    account.email = data['email']
                if 'password' in data:
                    account.password = data['password']
                if 'is_superuser' in data:
                    account.is_superuser = data['is_superuser']
                account.save()
                return JsonResponse({'id': account.id, 'username': account.username, 'email': account.email,
                                     'is_superuser': account.is_superuser})
            else:
                return JsonResponse({'error': 'Account not found'}, status=404)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')

    elif request.method == 'DELETE':
        # Assurez-vous qu'un ID est fourni
        if not pk:
            return HttpResponseBadRequest('Account ID is required for DELETE request')
        account = Account.objects.filter(id=pk).first()
        if account:
            account.delete()
            return JsonResponse({'message': 'Account deleted successfully'}, status=204)
        else:
            return JsonResponse({'error': 'Account not found'}, status=404)

    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])

@csrf_exempt
def manage_questions(request, pk=None):
    if request.method == 'GET':
        # Si un ID est fourni, récupérer la question spécifique
        if pk:
            question = Question.objects.filter(id=pk).values('id', 'category', 'question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer')
            if question.exists():
                return JsonResponse(list(question)[0])
            else:
                return JsonResponse({'error': 'Question not found'}, status=404)
        # Sinon, récupérer toutes les questions
        else:
            questions = Question.objects.all().values('id', 'category', 'question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer')
            questions_list = list(questions)
            return JsonResponse(questions_list, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Vérifier que toutes les données requises sont présentes
            if all(key in data for key in ['category', 'question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer']):
                question = Question.objects.create(
                    category=data['category'],
                    question_text=data['question_text'],
                    answer_1=data['answer_1'],
                    answer_2=data['answer_2'],
                    answer_3=data['answer_3'],
                    answer_4=data['answer_4'],
                    correct_answer=data['correct_answer']
                )
                return JsonResponse({'id': question.id, 'category': question.category, 'question_text': question.question_text,
                                     'answer_1': question.answer_1, 'answer_2': question.answer_2,
                                     'answer_3': question.answer_3, 'answer_4': question.answer_4,
                                     'correct_answer': question.correct_answer}, status=201)
            else:
                return JsonResponse({'error': 'Missing required fields'}, status=400)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')

    elif request.method == 'PUT':
        # Assurez-vous qu'un ID est fourni
        if not pk:
            return HttpResponseBadRequest('Question ID is required for PUT request')
        try:
            data = json.loads(request.body)
            question = Question.objects.filter(id=pk).first()
            if question:
                # Mettre à jour les champs fournis
                if 'category' in data:
                    question.category = data['category']
                if 'question_text' in data:
                    question.question_text = data['question_text']
                if 'answer_1' in data:
                    question.answer_1 = data['answer_1']
                if 'answer_2' in data:
                    question.answer_2 = data['answer_2']
                if 'answer_3' in data:
                    question.answer_3 = data['answer_3']
                if 'answer_4' in data:
                    question.answer_4 = data['answer_4']
                if 'correct_answer' in data:
                    question.correct_answer = data['correct_answer']
                question.save()
                return JsonResponse({'id': question.id, 'category': question.category, 'question_text': question.question_text,
                                     'answer_1': question.answer_1, 'answer_2': question.answer_2,
                                     'answer_3': question.answer_3, 'answer_4': question.answer_4,
                                     'correct_answer': question.correct_answer})
            else:
                return JsonResponse({'error': 'Question not found'}, status=404)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON format')

    elif request.method == 'DELETE':
        # Assurez-vous qu'un ID est fourni
        if not pk:
            return HttpResponseBadRequest('Question ID is required for DELETE request')
        question = Question.objects.filter(id=pk).first()
        if question:
            question.delete()
            return JsonResponse({'message': 'Question deleted successfully'}, status=204)
        else:
            return JsonResponse({'error': 'Question not found'}, status=404)

    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])