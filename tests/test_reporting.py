"""Tests for charminder.reporting module."""

from charminder.reporting import print_encoding_report


class TestPrintEncodingReport:
    """Test the reporting functionality."""

    def test_valid_encoding_no_issues(self, capsys):
        """Test report for valid encoding with no issues."""
        print_encoding_report("test.txt", [], "utf-8", is_valid=True)

        captured = capsys.readouterr()
        assert "✓ test.txt: Valid utf-8 encoding" in captured.out

    def test_valid_encoding_with_warnings(self, capsys):
        """Test report for valid encoding with warnings only."""
        issues = [
            {
                "type": "encoding_mismatch",
                "detected": "utf-8-sig",
                "expected": "utf-8",
                "confidence": 0.95,
                "message": "Detected encoding differs",
            },
        ]

        print_encoding_report("test.txt", issues, "utf-8", is_valid=True)

        captured = capsys.readouterr()
        assert "⚠ test.txt: Valid utf-8 encoding (with warnings)" in captured.out
        assert (
            "Warning: Detected utf-8-sig encoding (confidence: 95.00%)" in captured.out
        )

    def test_invalid_encoding_with_errors(self, capsys):
        """Test report for invalid encoding with errors."""
        issues = [
            {
                "type": "encode_error",
                "character": "🌍",
                "unicode_codepoint": "U+1F30D",
                "line": 1,
                "column": 7,
                "context": "Hello 🌍 world",
            },
        ]

        print_encoding_report("test.txt", issues, "ascii", is_valid=False)

        captured = capsys.readouterr()
        assert "✗ test.txt: Invalid ascii encoding" in captured.out
        assert "Invalid character '🌍' (U+1F30D) at line 1, column 7" in captured.out
        assert "Context: ...Hello 🌍 world..." in captured.out

    def test_decode_error_report(self, capsys):
        """Test report for decode errors."""
        issues = [
            {
                "type": "decode_error",
                "encoding": "ascii",
                "position": 5,
                "message": "Cannot decode byte b'\\xff' at position 5",
            },
        ]

        print_encoding_report("test.txt", issues, "ascii", is_valid=False)

        captured = capsys.readouterr()
        assert "✗ test.txt: Invalid ascii encoding" in captured.out
        assert "Decode error: Cannot decode byte b'\\xff' at position 5" in captured.out

    def test_detection_failed_error(self, capsys):
        """Test report for encoding detection failure."""
        issues = [
            {
                "type": "detection_failed",
                "message": "Could not detect file encoding",
            },
        ]

        print_encoding_report("test.txt", issues, "utf-8", is_valid=False)

        captured = capsys.readouterr()
        assert "✗ test.txt: Invalid utf-8 encoding" in captured.out
        assert "Error: Could not detect file encoding" in captured.out

    def test_file_error_report(self, capsys):
        """Test report for file reading errors."""
        issues = [
            {
                "type": "file_error",
                "message": "Error reading file: Permission denied",
            },
        ]

        print_encoding_report("test.txt", issues, "utf-8", is_valid=False)

        captured = capsys.readouterr()
        assert "✗ test.txt: Invalid utf-8 encoding" in captured.out
        assert "Error: Error reading file: Permission denied" in captured.out

    def test_multiple_issues_report(self, capsys):
        """Test report with multiple different types of issues."""
        issues = [
            {
                "type": "encode_error",
                "character": "🌍",
                "unicode_codepoint": "U+1F30D",
                "line": 1,
                "column": 7,
                "context": "Hello 🌍 world",
            },
            {
                "type": "encode_error",
                "character": "é",
                "unicode_codepoint": "U+00E9",
                "line": 2,
                "column": 3,
                "context": "café",
            },
            {
                "type": "encoding_mismatch",
                "detected": "utf-8",
                "expected": "ascii",
                "confidence": 0.99,
                "message": "Detected encoding differs",
            },
        ]

        print_encoding_report("test.txt", issues, "ascii", is_valid=False)

        captured = capsys.readouterr()
        output = captured.out

        assert "✗ test.txt: Invalid ascii encoding" in output
        assert "Invalid character '🌍'" in output
        assert "Invalid character 'é'" in output
        assert "Warning: Detected utf-8 encoding" in output

    def test_url_path_in_report(self, capsys):
        """Test that URL paths are handled correctly in reports."""
        url = "https://example.com/test.txt"
        print_encoding_report(url, [], "utf-8", is_valid=True)

        captured = capsys.readouterr()
        assert f"✓ {url}: Valid utf-8 encoding" in captured.out

    def test_output_ends_with_newline(self, capsys):
        """Test that all reports end with a newline for proper formatting."""
        # Test valid case
        print_encoding_report("test.txt", [], "utf-8", is_valid=True)
        captured = capsys.readouterr()
        assert captured.out.endswith("\n")

        # Test invalid case
        issues = [{"type": "file_error", "message": "Test error"}]
        print_encoding_report("test.txt", issues, "utf-8", is_valid=False)
        captured = capsys.readouterr()
        assert captured.out.endswith("\n\n")  # Extra newline after issue details
