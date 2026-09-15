@echo off
echo Starting Backend Server...
start cmd.exe /k "cd backend && ..\venv\Scripts\activate.bat && uvicorn app.main:app --host 127.0.0.1 --port 8000"

echo Starting Frontend Server...
start cmd.exe /k "cd frontend && npm run dev"

echo Enterprise Data Platform is starting!
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:5173
pause
