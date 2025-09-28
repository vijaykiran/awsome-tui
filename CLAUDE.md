# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AWSome is a Terminal User Interface (TUI) application for AWS built with Python using the Textual framework. It provides an interactive terminal interface for managing AWS resources.

## Development Commands

### Environment Setup
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync --all-extras --dev
```

### Running the Application
```bash
# Run the application
uv run awsome

# Or directly via Python module
uv run python -m awsome
```

### Code Quality Commands
```bash
# Run all quality checks (formatting, linting, type checking, tests)
./scripts/quality.sh

# Individual quality checks:
# Format code
uv run black src tests

# Lint code
uv run ruff check --fix src tests

# Type checking
uv run mypy src

# Run tests
uv run pytest tests

# Run tests with coverage
uv run pytest tests --cov=src/awsome --cov-report=term-missing --cov-report=html --cov-report=xml

# Run a single test file
uv run pytest tests/test_awsome_main.py

# Run a specific test
uv run pytest tests/test_awsome_main.py::TestAWSome::test_title
```

### Textual Development
```bash
# Run with dev console for debugging (requires textual-dev)
uv run textual run --dev src/awsome/main.py

# View Textual CSS reference
uv run textual colors
```

## Architecture

### Technology Stack
- **Python 3.12+**: Core language
- **Textual**: TUI framework for building terminal interfaces
- **boto3**: AWS SDK for Python
- **uv**: Package manager and virtual environment tool
- **pytest**: Testing framework with asyncio support

### Project Structure
```
src/awsome/          # Main application package
├── __init__.py
├── __main__.py      # Entry point for python -m awsome
├── main.py          # Main application class (AWSomeApp)
└── modules/         # Feature modules (new directory, currently empty)

tests/               # Test files
scripts/            
└── quality.sh       # Comprehensive quality check script

.github/workflows/
└── ci.yaml          # GitHub Actions CI pipeline
```

### Core Application Design

The application is built around `AWSomeApp` (inheriting from `textual.app.App`), which serves as the main application controller. The app uses Textual's reactive architecture for building responsive terminal interfaces.

Key architectural patterns:
- **Composition-based UI**: Uses Textual's `compose()` method to build UI hierarchically
- **Widget-based architecture**: UI components are Textual widgets (Header, Footer, custom widgets)
- **Async-first design**: Textual apps are inherently async, suitable for AWS API operations

### Code Standards

The project enforces strict code quality:
- **Black**: Code formatting (100 char line length)
- **Ruff**: Linting with selected rules (E, F, UP, B, SIM, I)
- **MyPy**: Strict type checking with no untyped definitions
- **pytest**: Required test coverage with async support

### Testing Strategy

- Tests use pytest with asyncio support (`pytest-asyncio`)
- Coverage reporting via pytest-cov
- Test files follow `test_*.py` naming convention
- CI runs tests on Python 3.12 and 3.13

## Important Notes

- Always use `uv run` to execute commands to ensure correct environment
- The `scripts/quality.sh` script runs all quality checks and should pass before committing
- The project uses strict type checking - all functions must have type hints
- When adding AWS functionality, boto3 client operations should be properly typed
- Textual widgets should be developed using the dev console for real-time debugging