from flask import Flask, request, render_template

app = Flask(__name__)

offers = [
  {
    "name": "Python Developer",
    "location":"Bengaluru, Karnataka",
    "salary": "1,25,000",
    "description": "You will be responsible for Design of software solutions based on requirements and within the constraints of architectural /design guidelines.",
  },
  {
    "name": "Python Big Data Developer",
    "location":"Bengaluru, Karnataka",
    "salary": "60,000",
    "description": "Our products and services are designed to empower the real-time data driven enterprise to help our clients win in the modern world of digital transformation.",
  },
  {
    "name": "Software Engineer",
    "location":"Bengaluru, Karnataka",
    "salary": "1,25,000",
    "description": "As a Software Engineering Manager at Indeed, you will provide hands-on leadership of a team of developers building integrations to partner systems. You will both contribute directly to building integrations, act as the point of contact for reviewing technical documentation for potential new integrations, and manage a combination of employees and contractors to deliver integrations.",
  },
  {
    "name": "Full Stack Developer",
    "location":"Bengaluru, Karnataka",
    "salary": "1,25,000",
    "description": "Excellent opportunity for a smart programmer who wants to be part of an education start up. You will be involved in back-end of an ecommerce-based portal and maintaining the same. You will be continuously upgrading the website with new features. This involves Payment Gateway, Web application, Backend process, Handling the database, Handling the server",
  },
  {
    "name": "Devops Enginee",
    "location":"Bengaluru, Karnataka",
    "salary": "1,25,000",
    "description": "We are looking for an experienced engineer to join our DevOps team with experience building a secure and scaling services in a cloud environment.",
  },
]

@app.route("/")
def home():
  return render_template("job-feed.html", len = len(offers) * 5, offers = offers * 5)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)