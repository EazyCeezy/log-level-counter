from count_levels import count_levels


def test_counts_each_level(tmp_path):
    log = tmp_path / "test.log"
    log.write_text("INFO a\nERROR b\nERROR c\nWARN d\n")
    assert count_levels(log) == {"INFO": 1, "WARN": 1, "ERROR": 2}


def test_skips_blank_lines(tmp_path):
    log = tmp_path / "test.log"
    log.write_text("INFO a\n\nERROR b\n")
    assert count_levels(log) == {"INFO": 1, "WARN": 0, "ERROR": 1}
