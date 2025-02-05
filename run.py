import setup
from time import sleep
from LINKEDIN import recommended_page
from LINKEDIN import search_jobs
from LINKEDIN import connect_people
from LINKEDIN import profile_stalker
from LINKEDIN import connect_recruiter

# first time setup
# creating a UI in python using pyqt6
# https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj

print("1. Let me login to the website.\n2. I am already logged in previously using this script.")
FIRST_SETUP = int(input())
if FIRST_SETUP == 1:
	# letting the user to login
	print("Chrome window will open to let you login to the accounts. \nYou have two minutes to login to your account :)")
	sleep(10)
	setup.loginWindow()
else:
	print("skipping setup...")

# ask the Service to automate

print("""
Which service to automate ?
1. Linkedin
0. Exit
	""")
SERVICE = int(input())

# ask input if required
if SERVICE == 2:
	print("No Service found! Ask the dev.")
elif SERVICE == 1:
	print("Linkedin Selected")
	print("""
Choose below ?
1. Apply Linkedin Recommended Jobs.
2. Search based on Position and Location.
3. Connect to Company People (paypal, nvidia, tesla, etc.)
4. Stalk Profiles (opens a link from profile you give, then keeps on.)
5. Connect to recruiter who is hiring certain position.
	""")
	LINKEDIN_SERVICE = int(input())
	if LINKEDIN_SERVICE == 1:
		print("Applying Linkedin Recommended Page..")
		rp = recommended_page.LinkedinBot()
		rp.click_easy_jobs()
	elif LINKEDIN_SERVICE == 2:
		print("Searching on Linkedin.")
		position = input("\nEnter post name\n")
		location = input("\nEnter job location\n")
		l = search_jobs.LinkedinBot()
		l.do_search(position, location)
		l.click_easy_jobs()
	elif LINKEDIN_SERVICE == 3:
		print("Connecting People on Linkedin.")
		co_name = input("\n Enter the company name in lowercase.\n")
		cp = connect_people.LinkedinBot(co_name)
		cp.connect()
	elif LINKEDIN_SERVICE == 4:
		print("Stalking People on Linkedin.")
		start_profile = input("\n Enter the Profile to start from.\n")
		ps = profile_stalker.LinkedinBot(start_profile)
		ps.stalk_on()
	elif LINKEDIN_SERVICE == 5:
		job_profile = input("\n enter position eg: 'python hiring'\n")
		print('Make sure to write about you in constants.py under variable LINKEDIN_CANDIDATE_INFO under 300 words')
		rp = connect_recruiter.LinkedinBot(job_profile=job_profile)
		rp.apply_job()
else:
	exit()



# if error, ask for going back to previous menu.

