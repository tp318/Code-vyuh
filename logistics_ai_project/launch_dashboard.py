import os
import subprocess
import sys

# Create Streamlit config directory
config_dir = os.path.expanduser('~/.streamlit')
os.makedirs(config_dir, exist_ok=True)

# Create config file to disable email prompt
config_file = os.path.join(config_dir, 'config.toml')
with open(config_file, 'w') as f:
    f.write('[browser]\ngatherUsageStats = false\n\n[server]\nheadless = true\n')

print("Streamlit configured. Running dashboard...")

# Now run the Streamlit app
subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'streamlit_app.py'])
