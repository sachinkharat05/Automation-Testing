# 🚀 TFLComentor Automation Testing Suite

An end-to-end automation testing framework developed to test the **Transflower Learning (TFLComentor)** web application using Python, Playwright, Pytest, and the Page Object Model (POM) design pattern.

This framework automates important user workflows for Admin, SME (Subject Matter Expert), and Student roles.

The project focuses on improving testing efficiency, reducing manual testing effort, and validating application functionality through browser automation.

---

## 📌 Project Overview

**Project Name:** TFLComentor Automation Testing Suite

**Application:** Transflower Learning (TFLComentor)

**Testing Type:** End-to-End (E2E) Automation Testing

**Framework:** Playwright with Pytest

**Design Pattern:** Page Object Model (POM)

**Programming Language:** Python

---

## 🛠️ Technologies & Tools Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution and test management |
| Page Object Model | Maintainable test architecture |
| Git | Version control |
| GitHub | Source code repository |
| Virtual Environment | Dependency isolation |
| pytest.ini | Pytest configuration |
| requirements.txt | Project dependencies |

---

## 🏗️ Framework Architecture

This automation framework follows the **Page Object Model (POM)** design pattern.

POM separates web page elements and actions from test scenarios.

### 1. Page Object Model (POM)

Page classes contain:

- Web element locators
- Page navigation methods
- User interaction methods
- Reusable page actions

Test classes contain:

- Test scenarios
- Workflow execution
- Assertions
- Test validation

This separation makes the framework easier to maintain, reuse, and extend.

### 2. Role-Based Testing

The framework supports three application roles:

- **Admin:** Assessment assignment and student management workflows.
- **SME:** Assessment creation and question management workflows.
- **Student:** Assessment navigation, answering, and submission workflows.

### 3. Reusable Login Functionality

The Login Page Object provides shared login functionality for different user roles.

This reduces duplicate login code and makes authentication workflows easier to maintain.

### 4. Browser Automation

Playwright is used to automate browser interactions such as:

- Opening application pages
- Entering login credentials
- Clicking buttons
- Selecting options
- Navigating dashboards
- Submitting forms
- Validating application responses

---

## 📂 Project Structure

```text
TFLComentor_Testing/
│
├── pages/
│   │
│   ├── __init__.py
│   ├── login_page.py
│   ├── admin_dashboard_page.py
│   ├── sme_dashboard_page.py
│   └── student_dashboard_page.py
│
├── tests/
│   │
│   ├── __init__.py
│   ├── test_admin_flow.py
│   ├── test_sme_flow.py
│   └── test_student_flow.py
│
├── pytest.ini
├── .gitignore
├── requirements.txt
└── README.md
```

### Folder Description

| Folder/File | Description |
|---|---|
| `pages/` | Contains Page Object Model classes |
| `login_page.py` | Login functionality for application users |
| `admin_dashboard_page.py` | Admin dashboard actions |
| `sme_dashboard_page.py` | SME dashboard and assessment creation actions |
| `student_dashboard_page.py` | Student dashboard and assessment actions |
| `tests/` | Contains automated test cases |
| `test_admin_flow.py` | Admin workflow test scenarios |
| `test_sme_flow.py` | SME workflow test scenarios |
| `test_student_flow.py` | Student workflow test scenarios |
| `pytest.ini` | Pytest configuration |
| `.gitignore` | Excludes unnecessary files from Git |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |

---

## 👥 User Roles & Functionalities

### 1. Admin

The Admin role manages assessment assignments and student-related workflows.

**Functionalities Tested:**

- Admin login
- Admin dashboard navigation
- Assessment card selection
- Assessment assignment module
- Student selection
- Test selection
- Assignment status selection
- Assessment assignment submission

**Test File:**

```text
tests/test_admin_flow.py
```

### 2. SME (Subject Matter Expert)

The SME role manages assessment creation and question configuration.

**Functionalities Tested:**

- SME login
- SME dashboard navigation
- Test creation interface
- Assessment duration configuration
- Difficulty level selection
- Subject domain configuration
- Question creation
- Multiple-choice option configuration
- Correct answer selection
- Question saving

**Test File:**

```text
tests/test_sme_flow.py
```

### 3. Student

The Student role participates in assigned assessments.

**Functionalities Tested:**

- Student login
- Student dashboard navigation
- Dashboard metrics validation
- Upcoming assessments navigation
- Scheduled assessment selection
- Assessment start functionality
- Question navigation
- Answer selection
- Assessment submission

**Test File:**

```text
tests/test_student_flow.py
```

---

## 🧪 Test Coverage

| Test Scenario | Test File |
|---|---|
| Admin Login | `test_admin_flow.py` |
| Admin Dashboard Navigation | `test_admin_flow.py` |
| Assessment Assignment | `test_admin_flow.py` |
| Student Selection | `test_admin_flow.py` |
| SME Login | `test_sme_flow.py` |
| Assessment Creation | `test_sme_flow.py` |
| Question Creation | `test_sme_flow.py` |
| Multiple-Choice Configuration | `test_sme_flow.py` |
| Student Login | `test_student_flow.py` |
| Student Dashboard Navigation | `test_student_flow.py` |
| Upcoming Assessments | `test_student_flow.py` |
| Assessment Start | `test_student_flow.py` |
| Answer Selection | `test_student_flow.py` |
| Assessment Submission | `test_student_flow.py` |

**Note:** The test scenarios listed above describe the intended coverage. Actual execution results depend on the implemented test cases and application availability.

---

## ⚙️ Prerequisites

Before running this project, install the following:

- Python 3.13 or compatible Python version
- Git
- Visual Studio Code or another Python editor
- Internet connection for dependency installation
- Access to the TFLComentor application
- Valid test accounts for Admin, SME, and Student roles

Verify Python installation:

```powershell
python --version
```

Verify Git installation:

```powershell
git --version
```

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

Replace the repository URL with your actual GitHub repository URL.

```powershell
git clone https://github.com/YOUR_USERNAME/TFLComentor_Testing.git
```

Navigate to the project directory:

```powershell
cd TFLComentor_Testing
```

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

After activation, the terminal should display:

```text
(venv)
```

### Step 4: Install Dependencies

```powershell
python -m pip install --upgrade pip
```

Install project dependencies:

```powershell
pip install -r requirements.txt
```

### Step 5: Install Playwright Browsers

Install Chromium:

```powershell
playwright install chromium
```

To install all supported Playwright browsers:

```powershell
playwright install
```

---

## 📦 Requirements

The `requirements.txt` file should contain the packages required by the project.

Example:

```text
pytest
playwright
pytest-playwright
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

**Important:** Keep `requirements.txt` aligned with the packages actually used in your framework. If the project uses additional libraries, include them as well.

---

## ▶️ How to Run Tests

Run the commands from the project root directory.

### 1. Run All Tests

```powershell
python -m pytest -v
```

### 2. Run All Tests with Print Statements

```powershell
python -m pytest -v -s
```

### 3. Run Admin Workflow

```powershell
python -m pytest tests/test_admin_flow.py -v -s
```

### 4. Run SME Workflow

```powershell
python -m pytest tests/test_sme_flow.py -v -s
```

### 5. Run Student Workflow

```powershell
python -m pytest tests/test_student_flow.py -v -s
```

### 6. Run a Specific Test Function

```powershell
python -m pytest tests/test_admin_flow.py::test_admin_login -v
```

Replace `test_admin_login` with the actual test function name.

### 7. Run Tests in Headed Browser Mode

If the test framework uses the Pytest Playwright plugin:

```powershell
python -m pytest --headed -v
```

### 8. Run Tests in Headless Mode

```powershell
python -m pytest --browser chromium -v
```

The browser mode depends on your Playwright and Pytest configuration.

---

## 🖥️ Browser Automation

Playwright automates browser interactions using Python.

Example:

```python
from playwright.sync_api import Page, expect


def test_homepage(page: Page):

    page.goto("https://your-application-url.com")

    expect(page).to_have_title("Your Application Title")
```

This example demonstrates:

1. Opening the application.
2. Loading the homepage.
3. Validating the page title.

Replace the example URL and title with the actual application values.

---

## 📊 Test Execution Reports

Pytest provides detailed execution information in the terminal.

Run:

```powershell
python -m pytest -v
```

Example output:

```text
============================= test session starts =============================

tests/test_admin_flow.py ........ PASSED
tests/test_sme_flow.py ......... PASSED
tests/test_student_flow.py ...... PASSED

============================= test session finished ===========================
```

The output above is an illustrative example, not an actual execution result.

### Generate an HTML Report

Install the reporting plugin:

```powershell
pip install pytest-html
```

Generate the report:

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

Create the reports directory before execution if it does not exist:

```powershell
mkdir reports
```

The generated report can be opened in a browser.

---

## 🔐 Test Credentials & Security

Application credentials are required for role-based testing.

For security reasons, **do not publish real usernames, phone numbers, or passwords in a public GitHub repository.**

Use environment variables or a local configuration file excluded from Git.

Example environment variables:

```text
ADMIN_USERNAME=your_admin_username
ADMIN_PASSWORD=your_admin_password

SME_USERNAME=your_sme_username
SME_PASSWORD=your_sme_password

STUDENT_USERNAME=your_student_username
STUDENT_PASSWORD=your_student_password
```

Never commit real credentials to GitHub.

If credentials have already been published, change them and remove them from the repository history where appropriate.

---

## 🧹 Git & GitHub

Check repository status:

```powershell
git status
```

Add project files:

```powershell
git add .
```

Commit changes:

```powershell
git commit -m "Add TFLComentor automation testing framework"
```

Push changes:

```powershell
git push origin main
```

---

## 📄 Recommended .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual Environment
venv/
.venv/

# Environment Variables
.env

# Pytest
.pytest_cache/

# Test Reports
reports/
test-results/

# Playwright
playwright/.cache/

# IDE
.vscode/

# Logs
*.log

# Operating System
.DS_Store
Thumbs.db
```

Review `.gitignore` before committing to ensure that important project files are not excluded.

---

## 🎯 Project Objectives

The main objectives of this automation framework are:

- Automate application testing using Playwright.
- Validate Admin, SME, and Student workflows.
- Reduce repetitive manual testing.
- Improve test execution efficiency.
- Implement the Page Object Model design pattern.
- Create reusable page actions.
- Improve test maintainability.
- Support repeatable end-to-end testing.
- Maintain the framework using Git and GitHub.

---

## 🔮 Future Enhancements

The framework can be extended with:

- Data-driven testing
- Parameterized test cases
- Negative login scenarios
- Cross-browser testing
- Screenshot capture on failure
- Playwright trace collection
- Logging
- CI/CD integration with GitHub Actions
- Automated HTML reports
- Environment-based configuration
- API testing integration

---

## 👨‍💻 Author

**Sachin Kharat**

Automation Testing | Python | Playwright | Pytest | Page Object Model

---

## ⭐ Conclusion

The TFLComentor Automation Testing Suite provides a structured approach to automating important application workflows.

By combining Python, Playwright, Pytest, and the Page Object Model design pattern, the framework supports reusable browser automation, organized test scenarios, and maintainable end-to-end testing.

The project demonstrates practical knowledge of browser automation, role-based testing, test framework architecture, and software quality assurance.

---

**Thank you for visiting the TFLComentor Automation Testing Suite!** 🚀
