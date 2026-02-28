from flask import Flask, request, render_template_string, redirect, session
import sqlite3



app = Flask(__name__)
app.secret_key = "piggyy_secret"

# Initialize database
def init_db():
    conn = sqlite3.connect("piggyy.db")
    c = conn.cursor()

    c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT,
    savings INTEGER DEFAULT 0,
    goal INTEGER DEFAULT 0,
    emergency_used INTEGER DEFAULT 0
)
""")

    conn.commit()
    conn.close()

init_db()
REGISTER_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Piggyy Register</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

body {
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #ff9ed8, #c084fc);
    font-family: 'Quicksand', sans-serif;
}

.register-card {
    background: white;
    padding: 50px;
    width: 370px;
    border-radius: 30px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    text-align: center;
}

h2 {
    font-family: 'Pacifico', cursive;
    color: #ff1493;
    font-size: 40px;
    margin-bottom: 20px;
}

input {
    width: 85%;
    padding: 12px;
    margin: 10px 0;
    border-radius: 20px;
    border: 2px solid #ffc0cb;
    text-align: center;
    font-size: 15px;
}

input:focus {
    outline: none;
    border-color: #ff69b4;
}

button {
    margin-top: 15px;
    padding: 12px 30px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(to right, #ff69b4, #c084fc);
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(255,105,180,0.5);
}

.error {
    color: red;
    margin-top: 10px;
}

a {
    display: block;
    margin-top: 15px;
    color: #ff1493;
    text-decoration: none;
    font-weight: 600;
}

a:hover {
    text-decoration: underline;
}

.pig {
    font-size: 50px;
    margin-bottom: 10px;
}
</style>
</head>

<body>

<div class="register-card">
<div class="pig">🐷</div>
<h2>MyPiggyy</h2>

<form method="POST">
    <input type="email" name="email" placeholder="Enter Email" required><br>
    <input type="password" name="password" placeholder="Create Password" required><br>
    <button type="submit">Register </button>
</form>

<p class="error">{{ message }}</p>

<a href="/login">Already have an account? Login </a>

</div>

</body>
</html>
"""
@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("piggyy.db")
        c = conn.cursor()

        try:
            c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            return redirect("/login")
        except:
            message = "User already exists!"
        conn.close()

    return render_template_string(REGISTER_PAGE, message=message)
LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Piggyy Login </title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

body {
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #ff9ed8, #c084fc);
    font-family: 'Quicksand', sans-serif;
}

.login-card {
    background: white;
    padding: 50px;
    width: 350px;
    border-radius: 30px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    text-align: center;
}

h2 {
    font-family: 'Pacifico', cursive;
    color: #ff1493;
    font-size: 40px;
    margin-bottom: 20px;
}

input {
    width: 85%;
    padding: 12px;
    margin: 10px 0;
    border-radius: 20px;
    border: 2px solid #ffc0cb;
    text-align: center;
    font-size: 15px;
}

input:focus {
    outline: none;
    border-color: #ff69b4;
}

button {
    margin-top: 15px;
    padding: 12px 30px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(to right, #ff69b4, #c084fc);
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(255,105,180,0.5);
}

.error {
    color: red;
    margin-top: 10px;
}

a {
    display: block;
    margin-top: 15px;
    color: #ff1493;
    text-decoration: none;
    font-weight: 600;
}

a:hover {
    text-decoration: underline;
}

.pig {
    font-size: 50px;
    margin-bottom: 10px;
}
</style>
</head>

<body>

<div class="login-card">
<div class="pig">🐷</div>
<h2>MyPiggyy</h2>

<form method="POST">
    <input type="email" name="email" placeholder="Enter Email" required><br>
    <input type="password" name="password" placeholder="Enter Password" required><br>
    <button type="submit">Login </button>
</form>

<p class="error">{{ message }}</p>

<a href="/">Don't have an account? Register 📝</a>

</div>

</body>
</html>
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("piggyy.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            goal = user[4]   # goal column index

            if goal == 0:
                return redirect("/setgoal")
            else:
                return redirect("/dashboard")
        else:
            message = "Invalid credentials!"

    return render_template_string(LOGIN_PAGE, message=message)
GOAL_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Set Your Goal </title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Indie+Flower&display=swap');

body {
    margin: 0;
    padding: 0;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(135deg, #ffc8dd, #ffafcc);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Indie Flower', cursive;
}

/* Center Card */
.goal-card {
    background: rgba(255, 255, 255, 0.9);
    padding: 60px;
    border-radius: 40px;
    text-align: center;
    box-shadow: 0 20px 50px rgba(255,105,180,0.4);
    z-index: 2;
}

h2 {
    font-family: 'Pacifico', cursive;
    color: #ff1493;
    font-size: 45px;
    margin-bottom: 20px;
}

p {
    font-size: 22px;
    margin-bottom: 20px;
}

input {
    padding: 12px;
    border-radius: 20px;
    border: 2px solid #ff69b4;
    text-align: center;
    font-size: 18px;
    width: 200px;
}

button {
    margin-top: 20px;
    padding: 12px 35px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(to right, #ff69b4, #ff1493);
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.1);
    box-shadow: 0 10px 25px rgba(255,20,147,0.5);
}

/* Coin Animation */
.coin {
    position: absolute;
    top: -50px;
    font-size: 30px;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(110vh);
    }
}

/* Random positions */
.coin:nth-child(1) { left: 10%; animation-duration: 5s; }
.coin:nth-child(2) { left: 30%; animation-duration: 7s; }
.coin:nth-child(3) { left: 50%; animation-duration: 6s; }
.coin:nth-child(4) { left: 70%; animation-duration: 8s; }
.coin:nth-child(5) { left: 90%; animation-duration: 4s; }

</style>
</head>

<body>

<!-- Coins -->
<div class="coin">🪙</div>
<div class="coin">🪙</div>
<div class="coin">🪙</div>
<div class="coin">🪙</div>
<div class="coin">🪙</div>

<div class="goal-card">
    <h2>Set Your Saving Goal </h2>
    <p>What is your dream amount? ✨</p>

    <form method="POST">
        <input type="number" name="goal" placeholder="Enter amount" required><br>
        <button type="submit">Save My Goal 🐷</button>
    </form>
</div>

</body>
</html>
"""
@app.route("/setgoal", methods=["GET", "POST"])
def setgoal():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("piggyy.db")
    c = conn.cursor()
    user_id = session["user_id"]

    # Check if goal already set
    c.execute("SELECT goal FROM users WHERE id=?", (user_id,))
    current_goal = c.fetchone()[0]

    if current_goal != 0:
        conn.close()
        return redirect("/dashboard")

    if request.method == "POST":
        goal = int(request.form["goal"])
        c.execute("UPDATE users SET goal=?, emergency_used=0 WHERE id=?", (goal, user_id))
        conn.commit()
        conn.close()
        return redirect("/dashboard")

    conn.close()
    return render_template_string(GOAL_PAGE)
DASHBOARD_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Piggyy 💖</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');
/* Popup Overlay */
.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 105, 180, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    animation: fadeIn 0.4s ease;
    z-index: 999;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Popup Box */
.popup-box {
    background: white;
    padding: 40px;
    border-radius: 30px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(255,20,147,0.4);
    animation: popUp 0.4s ease;
}

@keyframes popUp {
    from { transform: scale(0.7); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

.popup-emoji {
    font-size: 50px;
    margin-bottom: 15px;
}

.popup-box h2 {
    color: #ff1493;
    font-family: 'Pacifico', cursive;
}

.popup-box p {
    color: #ff69b4;
    font-size: 18px;
}

.popup-box button {
    margin-top: 15px;
    padding: 10px 25px;
    border-radius: 20px;
    border: none;
    background: linear-gradient(to right, #ff69b4, #ff1493);
    color: white;
    font-weight: bold;
    cursor: pointer;
}

.popup-box button:hover {
    transform: scale(1.05);
}
body {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffd6e8, #ffeef5);
    font-family: 'Quicksand', sans-serif;
    text-align: center;
    overflow-x: hidden;
}

h1 {
    font-family: 'Pacifico', cursive;
    color: #ff69b4;
    font-size: 45px;
}

.goal-box {
    position: absolute;
    top: 25px;
    right: 40px;
    background: white;
    padding: 20px 35px;
    border-radius: 25px;
    box-shadow: 0 8px 20px rgba(255,105,180,0.3);
}

.goal-box h2 {
    margin: 0;
    color: #ff1493;
    font-size: 28px;
}

.goal-box h3 {
    margin: 5px 0 0;
    color: #ff69b4;
}

.container {
    margin-top: 120px;
}

.card {
    background: white;
    width: 400px;
    margin: 20px auto;
    padding: 30px;
    border-radius: 30px;
    box-shadow: 0 10px 30px rgba(255,182,193,0.4);
}

input {
    padding: 10px;
    border-radius: 15px;
    border: 2px solid #ffc0cb;
    width: 70%;
    text-align: center;
}

button {
    padding: 10px 20px;
    border-radius: 20px;
    border: none;
    background: #ff69b4;
    color: white;
    font-weight: bold;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background: #ff1493;
}

/* Progress bar */
.progress-bar {
    width: 80%;
    background: #ffe4ec;
    border-radius: 30px;
    margin: 20px auto;
    overflow: hidden;
    position: relative;
}

.progress {
    height: 30px;
    background: linear-gradient(to right, #ff69b4, #ff1493);
    width: {{ (total/goal*100) if goal>0 else 0 }}%;
    transition: width 0.6s ease-in-out;
}

.progress-text {
    position: absolute;
    width: 100%;
    top: 4px;
    font-weight: bold;
    color: white;
}

/* Animated SVG Pig */
.pig-container {
    margin-top: 30px;
    animation: floatPig 2.5s ease-in-out infinite;
}

@keyframes floatPig {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* Coin animation */
.coin {
    position: absolute;
    top: -50px;
    left: 50%;
    font-size: 30px;
    animation: drop 1s ease forwards;
    display: none;
}

@keyframes drop {
    0% { top: -50px; opacity: 0; }
    50% { opacity: 1; }
    100% { top: 20px; opacity: 0; }
}
<script>
function dropCoin() {
    const coin = document.getElementById("coin");
    coin.style.display = "block";
    coin.style.animation = "none";
    coin.offsetHeight;
    coin.style.animation = "drop 1s ease forwards";
}
</script>
/* FULL SCREEN OVERLAY */
#celebration-overlay {
    position: fixed;   /* THIS prevents layout shifting */
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(255, 182, 193, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;   /* makes sure it stays above everything */
    animation: fadeOut 5s forwards;
}

/* CENTER MESSAGE */
#goal-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(to right, #ff69b4, #c084fc);
    color: white;
    padding: 35px 60px;
    border-radius: 40px;
    font-size: 26px;
    font-weight: bold;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    z-index: 9999;
    display: none;
    transition: opacity 1s ease;
}

/* POP EFFECT */
@keyframes pop {
    from { transform: scale(0.5); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

/* FADE OUT AFTER 1 SECONDS */
@keyframes fadeOut {
    0% { opacity: 1; }
    80% { opacity: 1; }
    100% { opacity: 0; visibility: hidden; }
}
</style>

{% if emergency_success == "success" %}
<div id="emergencyPopup" class="popup-overlay">
    <div class="popup-box">
        <div class="popup-emoji">🚨🐷</div>
        <h2>Emergency Withdrawal Successful!</h2>
        <p>Use it wisely 💸You got this!</p>
        <button onclick="closePopup()">Okay </button>
    </div>
</div>
{% endif %}
{% if withdraw_success == "success" %}
<div id="withdrawPopup" class="popup-overlay">
    <div class="popup-box">
        <div class="popup-emoji">💸🐷</div>
        <h2>Withdrawal Successful!</h2>
        <p>Your money has been withdrawn safely </p>
        <button onclick="closeWithdraw()">Okay </button>
    </div>
</div>
{% endif %}

<script>
function closePopup() {
    document.getElementById("emergencyPopup").style.display = "none";
}
</script>
<script>
function closeWithdraw() {
    document.getElementById("withdrawPopup").style.display = "none";
}
</script>

</body>
</html>
</head>
<body>

<div class="goal-box">
    <h2>🎯 Goal: ₹{{ goal }}</h2>
    <h3>💰 Savings: ₹{{ total }}</h3>
</div>

<div class="container">

<h1>MyPiggyy 💖</h1>

<div class="progress-bar">
    <div class="progress"></div>
    <div class="progress-text">
        {{ ((total/goal*100)|int) if goal>0 else 0 }}%
    </div>
</div>

<div class="card">
    <h3>Deposit Money </h3>
    <form method="POST" onsubmit="dropCoin()">
        <input type="number" name="amount" required placeholder="Enter amount in ₹"><br>
        <button type="submit">Add Money</button>
    </form>
</div>

<div class="card">
    <h3>Withdraw 💸</h3>
    <a href="/withdraw">
        <button>Go to Withdraw Page</button>
    </a>
</div>

<div class="pig-container">
    <div id="coin" class="coin">🪙</div>

    <!-- Bouncing Pig Face -->
<svg width="180" height="160" viewBox="0 0 180 160">

  <!-- Head -->
  <circle cx="90" cy="85" r="60" fill="#ffb6c1"/>

  <!-- Small Ears -->
  <circle cx="50" cy="40" r="15" fill="#ffb6c1"/>
  <circle cx="130" cy="40" r="15" fill="#ffb6c1"/>

  <!-- Inner Ears -->
  <circle cx="50" cy="40" r="8" fill="#ff8fab"/>
  <circle cx="130" cy="40" r="8" fill="#ff8fab"/>

  <!-- Eyes -->
  <circle cx="70" cy="80" r="6" fill="#333"/>
  <circle cx="110" cy="80" r="6" fill="#333"/>

  <!-- Blush -->
  <circle cx="60" cy="100" r="8" fill="#ff8fab" opacity="0.6"/>
  <circle cx="120" cy="100" r="8" fill="#ff8fab" opacity="0.6"/>

  <!-- Nose -->
  <ellipse cx="90" cy="105" rx="20" ry="13" fill="#ff69b4"/>
  <circle cx="82" cy="105" r="3" fill="#333"/>
  <circle cx="98" cy="105" r="3" fill="#333"/>

</svg>
</div>

<br>
<a href="/logout">Logout</a>

</div>
{% if goal_reached %}
<div id="goal-popup">
    🎉 Hurray! Your Goal is Reached! 🐷💖
</div>
{% endif %}

<!-- Confetti Library -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

{% if goal_reached %}
<script>
window.onload = function() {

    // Show popup
    const popup = document.getElementById("goal-popup");
    popup.style.display = "block";

    // Confetti burst
    var duration = 1000;
    var end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 5,
            spread: 70,
            origin: { y: 0.6 }
        });
        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());

    // Hide popup after 1 seconds
    setTimeout(() => {
        popup.style.opacity = "0";
    }, 1000);
};
</script>
{% endif %}
</body>
</html>
"""

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    withdraw_success=request.args.get("withdraw")
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("piggyy.db")
    c = conn.cursor()
    user_id = session["user_id"]

    emergency_success = request.args.get("emergency")

    if request.method == "POST":
        amount = int(request.form["amount"])
        c.execute("UPDATE users SET savings = savings + ? WHERE id=?", (amount, user_id))
        conn.commit()
        conn.close()

        # 🔥 IMPORTANT: Clean redirect
        return redirect("/dashboard")

    # GET request
    c.execute("SELECT savings, goal FROM users WHERE id=?", (user_id,))
    data = c.fetchone()

    total = data[0]
    goal = data[1]
    goal_reached=False
    if goal and total >= goal:
        goal_reached = True
    conn.close()

    return render_template_string(
        DASHBOARD_PAGE,
        total=total,
        goal=goal,
        emergency_success=emergency_success,goal_reached=goal_reached,withdraw_success=withdraw_success
    )
WITHDRAW_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Withdraw 💸</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

body {
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #ffd6e8, #ffeef5);
    font-family: 'Quicksand', sans-serif;
    text-align: center;
    overflow: hidden;
}

/* Floating Title */
h1 {
    font-family: 'Pacifico', cursive;
    color: #ff1493;
    font-size: 45px;
    margin-top: 40px;
    animation: floatTitle 2s ease-in-out infinite;
}

@keyframes floatTitle {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

/* Card */
.withdraw-card {
    background: white;
    width: 420px;
    margin: 40px auto;
    padding: 40px;
    border-radius: 35px;
    box-shadow: 0 15px 40px rgba(255,105,180,0.3);
}

.info {
    font-size: 18px;
    margin-bottom: 10px;
    color: #ff69b4;
}

input {
    padding: 12px;
    border-radius: 20px;
    border: 2px solid #ffc0cb;
    width: 70%;
    text-align: center;
    font-size: 16px;
}

button {
    margin-top: 15px;
    padding: 12px 25px;
    border-radius: 25px;
    border: none;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
    width: 80%;
}

/* Normal button */
.normal-btn {
    background: linear-gradient(to right, #ff69b4, #ff1493);
    color: white;
}

.normal-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(255,20,147,0.5);
}

/* Emergency button */
.emergency-btn {
    background: linear-gradient(to right, #ff4d6d, #c9184a);
    color: white;
}

.emergency-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(201,24,74,0.5);
}

.error {
    color: red;
    margin-top: 15px;
    font-weight: bold;
}

/* Floating coins */
.coin {
    position: absolute;
    top: -40px;
    font-size: 28px;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(110vh);
    }
}

.coin:nth-child(1) { left: 15%; animation-duration: 6s; }
.coin:nth-child(2) { left: 40%; animation-duration: 8s; }
.coin:nth-child(3) { left: 70%; animation-duration: 7s; }
.coin:nth-child(4) { left: 85%; animation-duration: 5s; }

a {
    display: block;
    margin-top: 20px;
    text-decoration: none;
    color: #ff1493;
    font-weight: bold;
}

a:hover {
    text-decoration: underline;
}
</style>
</head>

<body>

<!-- Floating coins -->
<div class="coin">🪙</div>
<div class="coin">🪙</div>
<div class="coin">🪙</div>
<div class="coin">🪙</div>

<h1>Withdraw Money 💸</h1>

<div class="withdraw-card">

    <div class="info">🎯 Goal: ₹{{ goal }}</div>
    <div class="info">💰 Savings: ₹{{ total }}</div>

    <form method="POST">
        <br>
        <input type="number" name="amount" required placeholder="Enter amount in ₹"><br><br>

        <button class="normal-btn" name="type" value="normal">
            Normal Withdrawal 
        </button>

        <button class="emergency-btn" name="type" value="emergency">
            Emergency Withdrawal 🚨
        </button>
    </form>

    <div class="error">{{ message }}</div>

    <a href="/dashboard">⬅ Back to Dashboard</a>

</div>

</body>
</html>
"""
@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("piggyy.db")
    c = conn.cursor()
    user_id = session["user_id"]

    c.execute("SELECT savings, goal, emergency_used FROM users WHERE id=?", (user_id,))
    data = c.fetchone()

    total = data[0]
    goal = data[1]
    emergency_used = data[2]

    message = ""

    if request.method == "POST":
        amount = int(request.form["amount"])
        withdraw_type = request.form["type"]

        if amount > total:
            message = "Not enough balance!"

        elif withdraw_type == "normal":
            if total >= goal:
                new_balance = total - amount

                c.execute("UPDATE users SET savings = ? WHERE id=?", (new_balance, user_id))
                conn.commit()

        # If goal completed and balance becomes 0
                if new_balance == 0:
                    conn.close()
                    return redirect("/goal_completed")

                conn.close()
                return redirect("/dashboard?withdraw=success")
            else:
                message = "Goal not reached. Normal withdrawal not allowed."

        elif withdraw_type == "emergency":
            if emergency_used == 0:
                c.execute("""
            UPDATE users 
            SET savings = savings - ?, emergency_used = 1 
            WHERE id=?
        """, (amount, user_id))
                conn.commit()
                conn.close()
                return redirect("/dashboard?emergency=success")
            else:
                message = "Emergency withdrawal already used for this goal."

    conn.close()
    return render_template_string(WITHDRAW_PAGE,
                                  total=total,
                                  goal=goal,
                                  message=message)
@app.route("/goal_completed")
def goal_completed():
    if "user_id" not in session:
        return redirect("/login")

    return """
<!DOCTYPE html>
<html>
<head>
<title>Goal Completed 🎉</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: linear-gradient(135deg, #ffb3d9, #ffd6ec);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Quicksand', sans-serif;
    overflow: hidden;
}

/* Card */
.card {
    background: white;
    padding: 60px;
    border-radius: 40px;
    text-align: center;
    box-shadow: 0 20px 50px rgba(255,105,180,0.4);
    animation: pop 0.6s ease;
}

@keyframes pop {
    from { transform: scale(0.7); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

h1 {
    font-family: 'Pacifico', cursive;
    color: #ff1493;
    font-size: 45px;
}

p {
    font-size: 20px;
    color: #ff69b4;
}

/* Buttons */
button {
    margin-top: 15px;
    padding: 12px 30px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(to right, #ff69b4, #ff1493);
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.1);
}

/* Confetti */
.confetti {
    position: absolute;
    font-size: 25px;
    animation: fall linear infinite;
}

@keyframes fall {
    to { transform: translateY(110vh); }
}

.confetti:nth-child(1){ left:10%; animation-duration:5s; }
.confetti:nth-child(2){ left:30%; animation-duration:6s; }
.confetti:nth-child(3){ left:50%; animation-duration:4s; }
.confetti:nth-child(4){ left:70%; animation-duration:7s; }
.confetti:nth-child(5){ left:90%; animation-duration:5s; }

/* Bouncing Pig Face */
.pig {
    margin-top: 20px;
    font-size: 60px;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    0%{ transform: translateY(0); }
    50%{ transform: translateY(-15px); }
    100%{ transform: translateY(0); }
}
</style>
</head>

<body>

<div class="confetti">🎉</div>
<div class="confetti">💖</div>
<div class="confetti">✨</div>
<div class="confetti">🎊</div>
<div class="confetti">💸</div>

<div class="card">
    <h1>Goal Completed! 🎉</h1>
    <p>You smashed your savings goal 💕</p>

    <div class="pig">🐷</div>

    <br>
    <a href="/reset_goal"><button>Set New Goal 🎯</button></a>
    <br>
    <a href="/dashboard"><button>Keep Same Goal 💖</button></a>
</div>

</body>
</html>
"""
@app.route("/reset_goal")
def reset_goal():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("piggyy.db")
    c = conn.cursor()
    user_id = session["user_id"]

    # Now reset goal
    c.execute("UPDATE users SET goal = 0 WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

    return redirect("/setgoal")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
if __name__ == "__main__":
    app.run(debug=True)