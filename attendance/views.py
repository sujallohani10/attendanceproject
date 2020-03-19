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
    timesheetObj.date = date.today()
    timesheetObj.time_in = datetime.now().time()
    timesheetObj.status = 1
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
    cur_user_data = TimeSheet.objects.filter(user=request.user, date=today)

    # error message for not started shift for today
    if not cur_user_data:
        messages.info(request, "Start shift first!")
    else:
        # print(cur_user_data.values())
        time_in_obj = cur_user_data.values('time_in')
        time_in = time_in_obj[0]['time_in']
        time_in_mins = time_in.hour * 60 + time_in.minute  # converting time in minutes

        time_out = datetime.now().time()
        time_out_mins = time_out.hour * 60 + time_out.minute  # converting time in minutes

        # total hours worked
        total_hrs = format((time_out_mins - time_in_mins) / 60, '.2f')

        cur_user_data.update(time_out=time_out, num_of_hours = total_hrs)
        # success message
        messages.info(request, "Shift Ended for today Successfully!")
    return redirect('attendance')

def timeSheet(request):
    # User can view the timesheet of own
    pass