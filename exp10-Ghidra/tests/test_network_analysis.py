import sys
import subprocess
import os

HERE = os.path.dirname(os.path.dirname(__file__))
SCRIPT = os.path.join(HERE, 'scripts', 'network_analysis.py')
SAMPLE = os.path.join(HERE, 'samples', 'benign_sample1.bin')

def ensure_sample():
    if not os.path.exists(SAMPLE):
        gen = os.path.join(HERE, 'scripts', 'generate_dummy_sample.py')
        subprocess.run([sys.executable, gen, SAMPLE], check=True)

def test_network_analysis_finds_http_and_ip():
    ensure_sample()
    proc = subprocess.run([sys.executable, SCRIPT, SAMPLE], capture_output=True, text=True)
    assert proc.returncode == 0
    out = proc.stdout
    assert 'http' in out or 'http' in proc.stdout.lower()
    assert '192.0.2.45' in out
