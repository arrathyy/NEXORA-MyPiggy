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

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---


#### Build Photos

![Team](Add photo of your team here)


![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
