# case Win32
python -m venv venv
venv\Scripts\python.exe -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
venv\Scripts\python.exe -m pip install --no-cache-dir -r requirements.txt