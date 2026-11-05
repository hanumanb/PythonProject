from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "03_advanced"))
from importlib.machinery import SourceFileLoader

module = SourceFileLoader("retry_module", str(Path(__file__).parents[1] / "02_intermediate/20_unit_testing.py")).load_module()

def test_retry_delay_exponential_and_capped():
    assert module.retry_delay(0) == 1.0
    assert module.retry_delay(2) == 4.0
    assert module.retry_delay(10) == 30.0

def test_retry_delay_rejects_negative():
    try:
        module.retry_delay(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
