import pathlib

import pytest


REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "test-wheel-linux.yml"


def test_compute_matrix_validates_inputs():
    yaml = pytest.importorskip("yaml")
    workflow = yaml.safe_load(WORKFLOW.read_text())
    job = workflow["jobs"]["compute-matrix"]

    runs = "\n".join(step.get("run", "") for step in job["steps"])

    assert "Invalid host-platform" in runs, "host-platform validation missing"
    assert "Invalid test mode" in runs, "test-mode validation missing"
    assert "exit 1" in runs, "validation must fail the job on invalid input"
