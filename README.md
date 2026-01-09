# Rock Paper Scissors - CI/CD Pipeline Project

## 📋 Project Overview
This is a Python-based Rock Paper Scissors game with a complete CI/CD pipeline implementation for academic submission. The project demonstrates automated building, testing, and deployment using GitHub Actions.

## 📁 Project Structure
```
Rock_paper Game/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline configuration
│
├── rock_paper_scissor.py      # Main game application
├── test_game.py               # Unit tests using pytest
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)
```

## 🎮 Game Features
- Interactive command-line Rock Paper Scissors game
- Score tracking for player and computer
- Input validation
- Clean and modular code structure

## 🛠️ Technologies Used
- **Python 3.11**: Main programming language
- **pytest**: Testing framework
- **pytest-cov**: Code coverage reporting
- **flake8**: Code linting and syntax checking
- **GitHub Actions**: CI/CD automation

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd "Rock_paper Game"

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Application

### Run the game
```bash
python rock_paper_scissor.py
```

### Run tests
```bash
# Run all tests with verbose output
pytest test_game.py -v

# Run tests with coverage report
pytest test_game.py --cov=rock_paper_scissor --cov-report=term-missing
```

### Check code quality
```bash
# Check for syntax errors
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Full linting
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
```

## 🔄 CI/CD Pipeline

### Pipeline Architecture
The CI/CD pipeline consists of three sequential stages:

#### 1. **Build Stage** 🏗️
- Sets up Python 3.11 environment
- Installs project dependencies
- Performs syntax checking using flake8
- Validates code quality and identifies critical errors

#### 2. **Test Stage** 🧪
- Runs comprehensive unit tests with pytest
- Generates code coverage reports
- Fails the pipeline if any test fails
- Ensures all game logic functions correctly

#### 3. **Deploy Stage** 📦
- Packages the application into a distributable format
- Creates artifacts containing:
  - Main application file
  - Test suite
  - Dependencies list
- Uploads artifacts to GitHub Actions
- Retains artifacts for 30 days

### Workflow Triggers
The pipeline automatically runs on:
- Push to `main` branch
- Pull requests targeting `main` branch

### Workflow File Location
`.github/workflows/ci-cd.yml`

## 🧪 Test Coverage

The test suite (`test_game.py`) includes:

### Test Classes:
1. **TestDetermineWinner**: Tests all win/lose/draw scenarios
   - Player wins (rock vs scissor, paper vs rock, scissor vs paper)
   - Computer wins (all inverse scenarios)
   - Draw scenarios (matching choices)

2. **TestValidChoice**: Tests input validation
   - Valid choices (rock, paper, scissor)
   - Invalid inputs (empty strings, numbers, special characters)

3. **TestComputerChoice**: Tests random choice generation
   - Validates computer choices are always valid
   - Ensures randomness over multiple calls

4. **TestGameConstants**: Tests game configuration
   - Verifies GAME_WORDS contains all three options

**Total Test Cases**: 20+ test cases covering all game logic

## 📊 CI/CD Best Practices Implemented

✅ **Automated Testing**: Every code change is automatically tested  
✅ **Syntax Validation**: Code quality checks prevent syntax errors  
✅ **Sequential Stages**: Build → Test → Deploy ensures quality gates  
✅ **Artifact Management**: Packaged applications stored for deployment  
✅ **Fast Feedback**: Developers notified of failures immediately  
✅ **Isolated Environments**: Each job runs in clean Ubuntu environment  
✅ **Dependency Caching**: Optimized for faster pipeline execution  

## 🎓 Academic Justification

### Why This CI/CD Pipeline?

1. **Build Stage Purpose**:
   - Catches syntax errors before testing
   - Ensures dependencies install correctly
   - Validates code quality standards

2. **Test Stage Purpose**:
   - Prevents buggy code from reaching production
   - Ensures game logic works as expected
   - Provides code coverage metrics

3. **Deploy Stage Purpose**:
   - Automates packaging process
   - Creates deployable artifacts
   - Enables rollback to previous versions

### Key Learnings
- Automated pipelines reduce manual errors
- Testing prevents regression bugs
- Continuous integration improves code quality
- Artifact storage enables version control

## 📝 Requirements File Breakdown

```txt
pytest==7.4.3          # Testing framework
pytest-cov==4.1.0      # Coverage reporting
flake8==6.1.0          # Code linting
```

## 🔍 How to Verify Pipeline

1. Push code to `main` branch
2. Go to GitHub repository → Actions tab
3. Observe the three stages executing:
   - Build and Syntax Check ✓
   - Run Tests ✓
   - Package and Deploy ✓
4. Download artifacts from successful runs

## 🐛 Troubleshooting

### Common Issues:

**Tests fail locally**:
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt
```

**Import errors**:
```bash
# Run tests from project root directory
cd "Rock_paper Game"
pytest test_game.py -v
```

**Pipeline fails on GitHub**:
- Check that branch name is `main` (not `master`)
- Verify all files are committed and pushed
- Review GitHub Actions logs for specific errors

## 👨‍💻 Author
[Your Name]  
Semester Project - CI/CD Implementation

## 📄 License
This project is for academic purposes.

---

**Note**: This project demonstrates practical DevOps concepts including continuous integration, automated testing, and deployment automation suitable for academic evaluation and viva defense.
