import requests
import datetime
from django.http import JsonResponse
from django.shortcuts import render

# Constant for Codeforces logo

def contest(request):
    url = "https://codeforces.com/api/contest.list"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] != "OK":
            return JsonResponse({"error": "Failed to fetch contests"}, status=400)

        contests = data["result"]

        current_time = datetime.datetime.now(datetime.timezone.utc)

        contests.sort(key=lambda x: x["startTimeSeconds"], reverse=False)

        displayed_contests = []
        for contest in contests:
            if contest["phase"] != "BEFORE":
                continue

            start_time_utc = datetime.datetime.fromtimestamp(
                contest["startTimeSeconds"], datetime.timezone.utc
            )
            start_time_utc6 = start_time_utc + datetime.timedelta(hours=6)
            end_time_utc6 = start_time_utc6 + datetime.timedelta(seconds=contest["durationSeconds"])


            time_diff = start_time_utc - current_time

            # Calculate days until start (integer)
            days_until = time_diff.days

            contest_data = {
                "title": contest["name"],
                "start_date_utc6": start_time_utc6.strftime("%b/%d/%Y"),
                "start_time_utc6": start_time_utc6.strftime("%H:%M"),
                "end_time_utc6": end_time_utc6.strftime("%H:%M"),
                "days_until": days_until,
                "registration_link": f"https://codeforces.com/contests/{contest['id']}",
            }
            displayed_contests.append(contest_data)

            if len(displayed_contests) == 3:
                break

        return render(request, "contest/contest.html", {"contests": displayed_contests})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
