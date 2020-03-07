from datetime import date

from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import TimeSheet
from django.utils import timezone
from django.utils.timezone import datetime


# Create your views here.


def index(request):
    return render(request, 'index.html')


def startShift(request):
    # check user is authenticated or not
    if not request.user.is_authenticated:
        raise Http404
    timesheetObj = TimeSheet()
    timesheetObj.signin_datetime = datetime.today()
    timesheetObj.user = request.user
    timesheetObj.save()
    # success message
    messages.info(request, "Shift Started Successfully!")
    return redirect('attendance')


def endShift(request):
    # check user is authenticated user or not
    if not request.user.is_authenticated:
        raise Http404

    # first we need to check if current user has already started shift or not. If started, then only that user can
    # end shift
    today = date.today()
    cur_user_data = TimeSheet.objects.filter(user=request.user, signin_datetime__contains=today)

    # error message for not started shift for today
    if not cur_user_data:
        messages.info(request, "Shift not started for today!")
    else:
        cur_user_data.update(signout_datetime=datetime.today())
        # success message
        messages.info(request, "Shift Ended for today Successfully!")
    return redirect('attendance')

def timeSheet(request):
    # User can view the timesheet of own
    pass