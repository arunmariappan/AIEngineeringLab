@echo off
rem Start Claude Code with your CLASS key and the course model (Haiku 5.5).
rem Reads .env in this folder. Changes nothing in your own Claude Code setup,
rem and never prints your key. Extra arguments pass through, e.g.:
rem   claude-class.cmd --permission-mode plan
setlocal
cd /d "%~dp0"
if not exist ".env" (
  echo No .env file here. Copy .env.example to .env and paste your class key first.
  exit /b 1
)
for /f "usebackq eol=# tokens=1,* delims==" %%A in (".env") do set "%%A=%%B"
if not defined ANTHROPIC_API_KEY (
  echo Your .env has no ANTHROPIC_API_KEY line. Paste your class key into .env first.
  exit /b 1
)
rem Through the class gateway the key travels as a bearer token; direct keys stay as they are.
if defined ANTHROPIC_BASE_URL (
  set "ANTHROPIC_AUTH_TOKEN=%ANTHROPIC_API_KEY%"
  set "ANTHROPIC_API_KEY="
)
set "ANTHROPIC_MODEL=claude-haiku-5-5"
claude %*
