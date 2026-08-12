import pathlib

WORKFLOW = pathlib.Path(__file__).resolve().parents[1] / ".github" / "workflows" / "test-wheel-linux.yml"

def test_nvidia_visible_devices_has_default():
    text = WORKFLOW.read_text()
    assert "NVIDIA_VISIBLE_DEVICES:" in text
    assert "|| 'all'" in text
