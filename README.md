<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# MyPiggy 🎯

## Basic Details

### Team Name: Nexora

### Team Members
- Member 1: Arathy Vinod - TKM College of Engineering
- Member 2: Megha Suresh - TKM College of Engineering

### Hosted Project Link
[mention your project hosted link here]

### Project Description
MyPiggyy is a simple, goal-based web application designed to help students and hostelers save money without the formality of a traditional bank. Inspired by the childhood habit of using a physical piggy bank, Piggyy allows users to digitally "drop in" small amounts of money—like UPI transfers—and track their progress toward specific personal goals (like a new gadget, a trip, or an emergency fund).

### The Problem statement
Traditional banking is too formal and complex for simple habit-building, leaving students and others struggling with unintentional spending. Because our savings are mixed into our primary UPI accounts, there’s no boundary between 'spending' and 'saving.'

### The Solution
MyPiggyy provides a dedicated, non-intimidating space to separate "goal money" from "spending money," replacing complex financial jargon with a simple, visual progress bar to limit impulsive withdrawals and build long-term habits. By turning a boring financial chore into a rewarding, goal-driven achievement, Piggyy makes saving personal again.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: HTML, JavaScript, Python, CSS
- Frameworks used: Flask
- Libraries used: Flask, sqlite3, canvas-confetti
- Tools used:  VS Code, Git, Github, Python virtual environment, Chrome(web browser)


---

## Features

List the key features of your project:
- Jargon-Free Progress Tracking: We replaced complex bank statements and confusing transaction lists with a clean, visual progress bar. Built using JavaScript and CSS, this bar fills up in real-time as you log deposits, providing the same "heavy" feeling of a physical piggy bank getting full.
- Controlled "Emergency" Withdrawals: To solve the problem of mid-month "unintentional spending," Piggyy features a discipline-first withdrawal system. It allows users to access their funds if needed but tracks the frequency of withdrawals, encouraging them to think twice before "breaking the jar."
- Milestone Celebration System: Once a goal hits 100%, the app triggers a dedicated success animation and reward screen. This positive reinforcement is a key part of behavioral design.
- Immersive UI/UX Experience : The app uses animated SVG elements, floating pig icons, and falling coin animations to make the interface feel alive. It turns a "financial chore" into an engaging, non-intimidating experience for students.

---

## Implementation

### For Software:

#### Installation
```bash
pip install Flask
```

#### Run
```bash
python app.py
```


---

## Project Documentation

### For Software:

#### Screenshots 

<img width="1917" height="1199" alt="set goal" src="https://github.com/user-attachments/assets/a29d57c3-aae2-43ba-9985-38a5a9d87aed" />
Set your dream savings goal.

<img width="1919" height="1198" alt="goal reached" src="https://github.com/user-attachments/assets/3b92b61b-9b73-472e-a934-3795b48bf953" />
Goal achieved and time to celebrate.

<img width="1919" height="1199" alt="withdrawal successfull" src="https://github.com/user-attachments/assets/f6b4e506-2ceb-44cd-bcaa-7915716c04c8" />
Money withdrawed successfully.

<img width="1919" height="1199" alt="emergency withdrawal" src="https://github.com/user-attachments/assets/3c975205-e8a9-46c8-b25d-9515f22490b8" />
Emergency withdrawal successfull.

#### Diagrams

**System Architecture:**

![system architecture](https://github.com/user-attachments/assets/ec7ec143-0536-4f4c-8953-fb7ac996fe81)

The MyPiggyy application follows a classic three-tier architecture consisting of the User Interface (Frontend), Backend (Flask), and Database (SQLite). The frontend, built with HTML, CSS, and JavaScript, provides pages for registration, login, setting a savings goal, depositing money, and making withdrawals, including emergency withdrawals. Users interact with the frontend through HTTP requests, which are sent to the Flask backend, responsible for handling business logic such as validating inputs, managing sessions, enforcing withdrawal rules, updating goals and savings...The backend interacts with the SQLite database via SQL queries to store and retrieve user information, savings balances, goals, and transaction records. Data flows from the user’s actions on the frontend to the backend, where it is processed and then persisted in the database. Responses, such as updated savings totals, withdrawal confirmations, or error messages, are sent back to the frontend for real-time display. The tech stack ensures lightweight deployment, fast data access, and an interactive user experience, while key features like goal management, savings tracking, emergency withdrawals, and session handling are seamlessly integrated through coordinated frontend-backend-database interactions.

**Application Workflow:**![workflow](https://github.com/user-attachments/assets/1532d1b2-50a8-48b3-a6c9-fa0dbec41339)
Users set a savings goal and deposit money(goal locked),then can either unlock their savings upon goal completion or use the emergency withdrawel option anytime.



#Project Demo

https://drive.google.com/drive/folders/1wEFE0FKijZOg4dA_Zp55y9KGDbmZQeDr?usp=sharing

---


---

## Team Contributions

- Arathy Vinod:Frontend,Backend,UI Design
- Megha Suresh:Frontend,Backend,UI Design

---

---

Made with ❤️ at TinkerHub
