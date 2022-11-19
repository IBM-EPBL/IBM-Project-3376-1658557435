<h1 align='center'>Nutrition assistant Application</h1>

### Demo Link

- k8s cluster 1: [naa-app-on-cluster-1.com](http://159.122.174.233:30991/main/), (expires after: 30-11-22)
- k8s cluster 2: [naa-app-on-cluster-2.com](http://169.51.204.20:30634/main/), (expires after: 20-12-22)

### Demo Video Link

[Watch demo on youtube](https://youtu.be/JFRLPu-cDVw)

### Abstract

It can be very helpful and improve eating habits to develop app-based nutrient dashboard systems that can evaluate real-time photographs of meals and assess them for nutritional content. The health tracking platform must, like any other nutrition app, have a specific capability set as well as a number of fundamental elements that assist users in bettering their physical condition and set it apart from other apps currently on the market. Diet services can provide more than just calorie counting, food intake monitoring, and physical activity tracking. In addition, it offers food diaries, diet tracking, a health activity tracker, and diet plans for pregnancy, bodybuilding, and veganism. Even if the main goal was to design an app for a diet plan with proper nutrition, the platform must be adaptable to future changes and the addition of new features.

### Tasks

| Task | Source |
|---|---|
|**Setting Up Application Environment**|
| Create Flask Project | [view source](Project%20Development%20Phase/Sprint%201/app)
| Create IBM Cloud Account | [view source](Project%20Development%20Phase/Sprint%201/screenshots/accounts/IBM_account.png)
| Install IBM Cloud CLI | [view source](Project%20Development%20Phase/Sprint%201/screenshots/accounts/IBM_account.png)
| Docker CLI Installation | [view source](Project%20Development%20Phase/Sprint%201/screenshots/accounts/docker_cli.png)
| Create an account in sendgrid | [view source](https://www.courier.com/)
| _(sendgrid was not approved so we used [courier.com](https://www.courier.com/))_
| Create an account in Nutrition api _([spoonacular.com](https://spoonacular.com/food-api))_ | [view source](https://spoonacular.com/food-api)
| **Implementing Web Application** 
| Create UI to interact with Application | [view source](Project%20Development%20Phase/Sprint%202/app/templates)
| Create IBM DB2 And Connect with Python | [view source](Project%20Development%20Phase/Sprint%201/app/utils/db2.py)
| Integrate Nutrition API | [view source](Project%20Development%20Phase/Sprint%202/app/controllers/main_controller.py)
| **Integrate SendGrid Service** 
| SendGrid Integration with Python code | [view source](Project%20Development%20Phase/Sprint%201/app/utils/mail.py) 
| **Deployment of App in IBM Cloud**
| Containerize the App | [view source](Project%20Development%20Phase/Sprint%204)
| Upload image to IBM Container Registry | [view source](Project%20Development%20Phase/Sprint%204/screenshots/ibm_cr.png)
| Deploy in Kubernetes Cluster | [view source](Project%20Development%20Phase/Sprint%204)
| **Project Development Phase** 
| Project Development - Delivery of Sprint-1 | [view source](Project%20Development%20Phase/Sprint%201)
| Project Development - Delivery of Sprint-2 | [view source](Project%20Development%20Phase/Sprint%202)
| Project Development - Delivery of Sprint-3 | [view source](Project%20Development%20Phase/Sprint%203)
| Project Development - Delivery of Sprint-4 | [view source](Project%20Development%20Phase/Sprint%204)
