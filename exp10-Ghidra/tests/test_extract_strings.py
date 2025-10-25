import sys
import subprocess
import os

HERE = os.path.dirname(os.path.dirname(__file__))
SCRIPT = os.path.join(HERE, 'scripts', 'extract_strings.py')
SAMPLE = os.path.join(HERE, 'samples', 'benign_sample1.bin')

def ensure_sample():
    # If the sample doesn't exist, create it using the generator
    if not os.path.exists(SAMPLE):
        gen = os.path.join(HERE, 'scripts', 'generate_dummy_sample.py')
        subprocess.run([sys.executable, gen, SAMPLE], check=True)

def test_extract_strings_contains_known_templates():
    ensure_sample()
    proc = subprocess.run([sys.executable, SCRIPT, SAMPLE], capture_output=True, text=True)
    assert proc.returncode == 0
    out = proc.stdout
    assert 'This is a benign sample for analysis.' in out
    assert 'http://example.local/resource' in out
    assert 'CreateFileA' in out
