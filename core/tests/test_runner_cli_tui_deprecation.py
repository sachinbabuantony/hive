from framework.runner.cli import _print_tui_deprecation_notice


def test_tui_deprecation_notice_prints_to_stderr(capsys):
    _print_tui_deprecation_notice()

    captured = capsys.readouterr()
    assert "deprecated" in captured.err.lower()
    assert "hive open" in captured.err
