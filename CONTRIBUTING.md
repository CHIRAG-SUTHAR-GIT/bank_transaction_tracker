# Contributing to Account Summary Control Room

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Be respectful and constructive in all interactions. We are committed to providing a welcoming and inspiring community for all.

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- GitHub account

### Setting Up Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork:**
```bash
git clone https://github.com/your-username/ACCOUNT-SUMMARY-CONTROL-ROOM.git
cd ACCOUNT-SUMMARY-CONTROL-ROOM
```

3. **Add upstream remote:**
```bash
git remote add upstream https://github.com/Chirag-helpline16/ACCOUNT-SUMMARY-CONTROL-ROOM.git
```

4. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

5. **Install dependencies:**
```bash
pip install -r requirements.txt
pip install pytest black flake8 isort
```

## How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** using the Bug Report template
3. **Include:**
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots/logs if applicable

### Requesting Features

1. **Check open issues and discussions**
2. **Create a new issue** using the Feature Request template
3. **Describe:**
   - Problem being solved
   - Proposed solution
   - Alternative approaches
   - Use cases

### Code Contributions

1. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes:**
   - Keep commits logical and focused
   - Write clear commit messages
   - Add/update docstrings
   - Follow PEP 8 style guide

3. **Code Quality:**
```bash
# Format code with Black
black .

# Sort imports
isort .

# Check linting
flake8 . --max-line-length=100

# Run tests
pytest
```

4. **Keep your branch updated:**
```bash
git fetch upstream
git rebase upstream/main
```

5. **Push to your fork:**
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request:**
   - Use the PR template
   - Reference related issues (Fixes #123)
   - Provide clear description of changes
   - Request review from maintainers

## Code Standards

### Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable and function names

### Documentation
- Add docstrings to all functions and classes
- Use Google-style docstrings:
```python
def example_function(param1, param2):
    """Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When this exception occurs
    """
```

### Testing
- Write tests for new features
- Maintain or improve code coverage
- Run tests before submitting PR:
```bash
pytest --cov=. --cov-report=html
```

## Git Workflow

### Branch Naming Conventions
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test improvements

### Commit Messages
- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor to..." not "Moves cursor to..."
- Limit first line to 72 characters
- Reference issues and pull requests: "Fixes #123"

Example:
```
Add deduplication audit logging

- Log duplicate transactions to database
- Track excluded amounts per ACK
- Implement strict rebuild option

Fixes #45
```

## Review Process

1. **Automated Checks:**
   - Tests must pass
   - Code quality checks must pass
   - No merge conflicts

2. **Review:**
   - Maintainers will review code
   - May request changes
   - Provide constructive feedback

3. **Merge:**
   - Approved PRs will be merged
   - Commits are squashed for clean history

## Development Tips

### Running the Application
```bash
python app_account.py
```
Access at `http://localhost:5000`

### Running Tests
```bash
# All tests
pytest

# Specific test file
pytest tests/test_deduplication.py

# With coverage
pytest --cov=. --cov-report=html
```

### Debugging
- Use Python debugger: `import pdb; pdb.set_trace()`
- Check logs in `logs/` directory
- Enable Flask debug mode

### Database Management
```bash
# Reset database
python -c "from summary_database import init_db; init_db()"

# View database
sqlite3 data/account_summary.db ".tables"
```

## Documentation

### Updating Documentation
- Edit markdown files in the repository
- Keep documentation in sync with code
- Add examples and clarifications
- Update API documentation if endpoints change

### Building Documentation Locally
```bash
# If using Sphinx (optional)
cd docs
make html
```

## Community

### Communication Channels
- **Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Pull Requests**: Submit code changes
- **Email**: chirag.helpline16@example.com

### Getting Help
- Read the [README](README.md)
- Check [documentation](ACCOUNT_SUMMARY_BATCH_GUIDE.md)
- Search existing issues and discussions
- Ask in GitHub Discussions

## Project Structure Understanding

```
Key files for contributors:
- app_account.py: Flask application and API endpoints
- batch_account_summaries.py: Batch processing logic
- summary_database.py: Database operations
- templates/account_summary_dashboard.html: UI template
```

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

## Additional Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Thank you for contributing!** We appreciate your time and effort to improve this project.
