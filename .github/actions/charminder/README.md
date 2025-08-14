# CharMinder GitHub Action

A GitHub Action that checks character encoding issues in text files using [CharMinder](https://github.com/nelsonwmoore/CharMinder).

## Features

- ✅ **Multiple File Support**: Check multiple files using wildcards or specific paths
- 🌐 **URL Support**: Validate encoding of remote files and URLs
- 🎯 **Multiple Encodings**: Support for UTF-8, UTF-16, UTF-32, and ASCII
- 📊 **Detailed Reports**: Get precise character-level issue reporting
- 🔄 **CI/CD Integration**: Perfect for automated encoding validation in workflows

## Usage

### Basic Example

```yaml
- name: Check file encodings
  uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: '*.txt *.md'
    encoding: 'UTF8'
```

### Advanced Example

```yaml
- name: Check multiple file types
  uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: 'src/**/*.py docs/*.md *.json'
    encoding: 'UTF8'
    python-version: '3.11'
```

### With Error Handling

```yaml
- name: Check ASCII encoding (continue on error)
  uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: 'legacy/*.txt'
    encoding: 'ASCII'
  continue-on-error: true
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `files` | Space-separated list of files or URLs to check (supports wildcards) | ✅ Yes | - |
| `encoding` | Encoding type to check for (`UTF8`, `UTF16`, `UTF32`, `ASCII`) | ❌ No | `UTF8` |
| `python-version` | Python version to use | ❌ No | `3.11` |

## Outputs

| Output | Description |
|--------|-------------|
| `result` | Result of the encoding check (`success` or `failure`) |

## File Patterns

The action supports various file patterns:

- **Wildcards**: `*.txt`, `*.md`, `**/*.py`
- **Specific files**: `README.md`, `src/main.py`
- **Multiple patterns**: `*.txt *.md docs/*.rst`
- **URLs**: `https://example.com/file.txt`

## Complete Workflow Template

Create `.github/workflows/encoding-check.yml` in your repository:

```yaml
name: 'Encoding Check'

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  charminder:
    name: 'Check File Encodings'
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check file encodings
        uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
        with:
          files: '*.txt *.md *.json *.csv'
          encoding: 'UTF8'
```

## Encoding Types

- **UTF8**: Most common encoding for modern text files
- **UTF16**: Common for Windows text files
- **UTF32**: Less common, used for specific applications
- **ASCII**: Basic 7-bit encoding for simple text

## Error Handling

The action will:
- ❌ **Fail** if any files contain invalid characters for the specified encoding
- ✅ **Pass** if all files are valid for the specified encoding
- 📝 **Report** detailed information about any encoding issues found

Use `continue-on-error: true` in your workflow step if you want the workflow to continue even when encoding issues are found.

## Examples in Different Scenarios

### Documentation Files
```yaml
- uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: '*.md docs/**/*.rst README.txt'
    encoding: 'UTF8'
```

### Source Code
```yaml
- uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: 'src/**/*.py lib/**/*.js'
    encoding: 'ASCII'
```

### Data Files
```yaml
- uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: 'data/*.csv *.json config/*.yml'
    encoding: 'UTF8'
```

### Remote Files
```yaml
- uses: nelsonwmoore/CharMinder/.github/actions/charminder@main
  with:
    files: 'https://raw.githubusercontent.com/user/repo/main/data.txt'
    encoding: 'UTF8'
```

## Contributing

Found an issue or want to improve the action? Please contribute to the [CharMinder repository](https://github.com/nelsonwmoore/CharMinder)!


