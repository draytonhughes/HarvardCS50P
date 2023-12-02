from project import check_arguments, should_we_watch, how_old
import pytest

def test_check_arguments():
    with pytest.raises(SystemExit):
        check_arguments()

def test_should_we_watch():
    assert should_we_watch("95") == "Must Watch"
    assert should_we_watch("92") == "Need to Watch"
    assert should_we_watch("30") == "Pass"

def test_how_old():
    assert how_old("2000") == "Age 23"
    assert how_old("2021") == "Age 2"
    assert how_old("1950") == "Age 73"


