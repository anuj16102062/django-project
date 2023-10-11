from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserDetailsSerializer
def calculate_spam_percentage(cell_number):
    total_users = User.objects.count()
    span_user = User.objects.filter(mob_number=cell_number)
    spam_marked_users = User.objects.filter(spam_cell_numbers=span_user[0].id).count()

    if total_users == 0:
        return 0.0

    spam_percentage = spam_marked_users / total_users
    return spam_percentage

@api_view(['POST'])
def register_user(request):
    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def mark_cellular_spam(request):
    try:
        user_id = request.data.get('user_id')
        mob_number = request.data.get('mob_number')

        user = User.objects.get(pk=user_id)
        spam_user = User.objects.filter(mob_number=mob_number).first()

        if not spam_user:
            spam_user = User(mob_number=mob_number)
            spam_user.save()

        user.spam_cell_numbers.add(spam_user)
        
        return Response({'message': 'This Cellular Number Marked As Spam'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def search_user_by_name(request):
    try:
        user_id = request.query_params.get('user_id')
        name = request.query_params.get('name')

        users = User.objects.filter(name__icontains=name).exclude(pk=user_id)
        results = []

        for user in users:
            spam_percentage = calculate_spam_percentage(user.mob_number)
            results.append({'name': user.name, 'phone': user.mob_number, 'spam_percentage': spam_percentage})

        return Response({'result':results}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def search_user_by_phone(request):
    try:
        user_id = request.query_params.get('user_id')
        mob_number = request.query_params.get('mob_number')

        users = User.objects.filter(mob_number=mob_number)
        results = []

        for user in users:
            spam_percentage = calculate_spam_percentage(user.mob_number)
            results.append({'name': user.name, 'mob_number': user.mob_number, 'spam_percentage': spam_percentage})

        return Response({'result':results}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_user_details(request):
    try:
        user_id = request.query_params.get('user_id')
        req_user_id = request.query_params.get('req_user_id')

        req_user = User.objects.filter(pk=req_user_id).first()

        if not req_user:
            return Response({'error': 'Req User not found'}, status=status.HTTP_404_NOT_FOUND)

        is_registered_user = User.objects.filter(pk=user_id).exists()

        user_details = {
            'name': req_user.name,
            'phone': req_user.phone,
            'email': req_user.email if is_registered_user and req_user.contacts.filter(pk=user_id).exists() else None,
            'spam_percentage': calculate_spam_percentage(req_user.mob_number)
        }

        return Response(user_details, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_all_users(request):
    try:
        users = User.objects.all()
        serializer = UserDetailsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
