from django.shortcuts import render

from utils import fake


def generate_user_information(request):

    user = fake.Users().generate_users()

    return render(request, "generate_user_information.html", {"user_dict": user})
