import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email credentials
sender_email = ""
password = ""  # Use the app-specific password

# Define the SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Define the list of leads (email, name)
leads = [
    {"email: example@gmail.com" "name: "} # Duplicate
]

# Define the email subject and body template
subject = "The Government Needs Your Janitorial Services – Explore Contract Opportunities for Janitorial Services!"
body_template = """
Dear {name},

I hope this message finds you well. My name is Silvanus, and I am a consultant specializing in government contracts and business development. I am reaching out to discuss how your janitorial services can seize the significant opportunities available through government contracts.

Government contracts can be a game changer for your business, providing a consistent stream of clients and enhancing your brand's credibility. The demand for reliable janitorial services in government facilities is growing, and your business is ideally positioned to meet this need.

Here’s How We Can Work Together:

SAM.gov Registration: I will guide you through the process of registering on SAM.gov, the primary database for government contractors. This registration is essential for bidding on government contracts.

UEI and CAGE Code Generation: I will assist you in obtaining your Unique Entity Identifier (UEI) and Commercial and Government Entity (CAGE) codes, both of which are necessary for doing business with the federal government.

Capability Statement Design: Together, we will craft a compelling capability statement that effectively highlights your services, experience, and competitive advantages. This document is crucial for marketing your business to potential government clients.

Proposal Development: I will help you understand the proposal requirements and develop winning proposals tailored to specific government contracts.

Ongoing Support: Throughout the entire process, I will provide continuous support and insights into compliance, performance metrics, and relationship management with government agencies.

By navigating the government contracting landscape, you can unlock a consistent flow of clients and enhance your business’s growth potential. If you’re interested in taking your business to the next level with government contracts, please reply to this email. I am here to guide you through all the steps needed to secure government contracts and assure you of my support throughout the process.

Thank you for considering this opportunity. I look forward to helping you elevate your business through government contracts.

Best regards,

Silvanus Gregory.
"""

# Function to send an email to a lead
def send_email(to_email, to_name):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Format the body with the lead's name
        body = body_template.format(name=to_name)
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable security
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())
            print(f"Email sent to {to_name} at {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Send emails to each lead in the list
for lead in leads:
    send_email(lead["email"], lead["name"])
