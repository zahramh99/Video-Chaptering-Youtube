# Video Chaptering System

Automatically generates chapters for YouTube videos using topic modeling.

## Setup
1. Get YouTube API key and add to `config/api_keys.yaml`
2. Install dependencies:
```bash
pip install -r requirements.txt

Usage
python src/main.py

Enter YouTube URL when prompted. Chapters will be saved in outputs/chapters/.

#### 9. `.gitignore`
API keys
config/api_keys.yaml

Data files
data/raw/
outputs/

Python
pycache/
*.py[cod]
*.pyc

Environments
.env
.venv
venv/

To use:
1. Add your YouTube API key to `config/api_keys.yaml`
2. Run `pip install -r requirements.txt`
3. Execute with `python src/main.py`