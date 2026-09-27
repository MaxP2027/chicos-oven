# Chico's Oven

Flask bakery website first draft.

## Run the local website

Open this repository folder in VS Code. In Run and Debug, choose **Chico's Oven - Run Website**, then press **Ctrl + F5**.

Alternatively, run these commands in PowerShell from the repository folder:

```powershell
.\.venv\Scripts\python.exe -m pip install -r bakery/requirements.txt
.\.venv\Scripts\python.exe -m flask --app bakery/app.py run --port 5001
```

If you need to create the environment first, run `py -m venv .venv`.

Once Flask displays `Running on http://127.0.0.1:5001`, open the [local website preview](http://127.0.0.1:5001).

**This is a local preview, not a public website.** The link only works on the computer running Flask, while the server is running. Putting this link on GitHub does not host the app. If you see "connection refused," start Flask using one of the methods above.

Do not open HTML templates directly. Flask must render them to load the styling, images, and page content.

Note: running `bakery/app.py` directly uses port 5000 instead. The commands above and the VS Code launch configuration both use port 5001.

See [bakery/README.md](bakery/README.md) for the structure and image filenames.
