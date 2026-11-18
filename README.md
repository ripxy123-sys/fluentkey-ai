# FluentKey AI — Prototype v0.1

A small responsive web prototype for the first FluentKey AI milestone. It includes style selection, task selection, a text editor, a result area, and a FastAPI backend that calls the OpenAI Responses API.

## Important
- The browser demo works without an API key using simple demo transformations. These are NOT ChatGPT results.
- Real AI requests require an OpenAI API key and API billing. ChatGPT subscriptions do not include API usage.
- Keep the API key on the server. Never put it in HTML, JavaScript, an iOS app, or an Android app.
- Text is sent to your backend only after the user presses **Improve with AI**.
- This is a first prototype, not yet an installable iOS/Android keyboard.

## Run locally
Requires Python 3.10+.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\\Scripts\\activate

pip install -r requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` as an environment variable in your terminal (recommended), then run:

```bash
uvicorn server:app --reload
```

Open http://127.0.0.1:8000

For Windows PowerShell, set the key for the current terminal:
```powershell
$env:OPENAI_API_KEY="your_key_here"
uvicorn server:app --reload
```

## Next engineering milestones
1. Add user-selectable language and Malayalam-specific translation tests.
2. Add response parsing for corrected text plus explanation as separate fields.
3. Add rate limits, authentication, abuse protection, and cost controls.
4. Build Android IME in Kotlin using InputMethodService.
5. Build iOS Custom Keyboard Extension in Swift. AI networking requires Apple's open-access permission, which users must explicitly enable.
6. Add privacy policy, consent UI, deletion controls, and secure telemetry minimization.

## Architecture
- Companion app / prototype UI: HTML now; shared cross-platform app can follow.
- AI service: FastAPI server.
- Model: configured by `OPENAI_MODEL`; set to a model available to your API project.
- Native keyboards: separate platform-specific extensions because Android and iOS keyboard APIs differ.


## v0.2 PWA additions
This package includes a web-app manifest, SVG app icons, and a service worker for caching the app shell. Serve it over HTTPS to install it from Safari using Share → Add to Home Screen. API requests are deliberately excluded from offline caching.
