@ECHO OFF
set current_dir=%cd%
CALL C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
CALL conda activate new_env
CALL python -i main.py
PAUSE