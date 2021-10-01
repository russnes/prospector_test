from rest_framework import status, views
from rest_framework.response import Response
from . import models


def my_func(a):
    print(a)


class MyView(views.APIView):
    def get(self, request):
        user_id = request.user
        print(user_id)
        all_models = models.MyModel.objects.all()
        print(all_models)

        my_func(1, 1)
        models.doesnotexist()

        return Response(data={"status": "Success!"}, status=status.HTTP_200_OK)
