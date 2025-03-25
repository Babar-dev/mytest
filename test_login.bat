@echo off
cd /d C:\Users\Babar\Desktop\Database_Form_SQA_Automation\  <-- Actual Test Directory
pytest test_login.py --html=test_login_report.html --self-contained-html --log-cli-level=INFO
pause