import mail
import job

# Get the job list
job.getJob()

# Send the job list by email
mail.mailSender()

print("Job Alert sent successfully !")