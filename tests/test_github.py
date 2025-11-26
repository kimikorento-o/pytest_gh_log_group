"""Unit tests for Github class error handling."""
from unittest.mock import MagicMock
from source.github import Github


class TestGithubErrorHandling:
    """Tests for Github class error handling when stream is closed. For example with pytester"""

    def test_write_line_handles_closed_stream(self):
        """write_line should gracefully handle ValueError when stream is closed."""
        mock_reporter = MagicMock()
        mock_reporter.write_line.side_effect = ValueError("I/O operation on closed file")

        github = Github(reporter=mock_reporter)
        github.write_line("test data")

    def test_end_github_group_handles_closed_stream(self):
        """end_github_group should gracefully handle ValueError."""
        mock_reporter = MagicMock()
        mock_reporter.line.side_effect = ValueError("I/O operation on closed file")

        github = Github(reporter=mock_reporter)
        github._active_group = "test group"

        github.end_github_group()
