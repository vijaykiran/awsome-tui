#!/bin/bash

# Exit on any error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${BLUE}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Main quality checks
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}Running Code Quality Checks${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    print_error "uv is not installed. Please install it first."
    exit 1
fi

# Run Black formatter
print_step "Running Black formatter check..."
if uv run black --check src tests; then
    print_success "Black formatting check passed"
else
    print_error "Black formatting check failed"
    print_warning "Run 'uv run black src tests' to fix formatting"
    exit 1
fi
echo

# Run Ruff linter
print_step "Running Ruff linter..."
if uv run ruff check --fix src tests; then
    print_success "Ruff linting passed"
else
    print_error "Ruff linting failed"
    print_warning "Run 'uv run ruff check --fix src tests' to fix auto-fixable issues"
    exit 1
fi
echo

# Run MyPy type checker
print_step "Running MyPy type checker..."
if uv run mypy src; then
    print_success "MyPy type checking passed"
else
    print_error "MyPy type checking failed"
    exit 1
fi
echo

# Run tests with coverage
print_step "Running tests with coverage..."
if uv run pytest tests --cov=src/awsome --cov-report=term-missing --cov-report=html --cov-report=xml; then
    print_success "All tests passed"
    echo
    print_step "Coverage report generated:"
    echo "  - Terminal output above"
    echo "  - HTML report: htmlcov/index.html"
    echo "  - XML report: coverage.xml"
else
    print_error "Tests failed"
    exit 1
fi

echo
echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}All quality checks passed successfully! 🎉${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
