
import subprocess


file = "app_profiler.py"

subprocess.Popen(
    ["streamlit", "run", file], shell=True
)