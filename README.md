# ☕ KeepMeOn

### Your PC, awake when you need it.

Ever left your PC downloading a file, running a script, or completing a task, only to find it had gone to sleep at the worst possible moment? 💤

**KeepMeOn** is a small, free utility for Windows that prevents your PC from automatically entering sleep mode when you need it to stay awake. Everything is managed directly from the system tray, with no intrusive windows and no unnecessary complications.

> 🔌 Small app, peace of mind. Let your PC work while you focus on something else.

---

## ✨ Features

- 🚀 **Keep your PC awake** — prevents automatic system sleep while you work.
- 🖱️ **System tray control** — manage everything from the icon near the Windows clock.
- 🔄 **Enable or disable anytime** — toggle the feature with a simple click.
- 🧹 **Automatic restoration** — when the application exits, the normal power behavior is restored.
- 🪶 **Lightweight and unobtrusive** — no permanently open windows or complicated interfaces.
- 🆓 **Completely free** — a small project designed to be useful, without unnecessary extras.

## 🎯 Who is it for?

KeepMeOn can be useful when you are:

- 💻 Running scripts or programs that need to finish without interruptions.
- 📥 Downloading large files.
- 🔧 Performing maintenance tasks or long-running operations.
- 🖥️ Preventing your PC from automatically going to sleep while you work.

## 🛠️ Built with

KeepMeOn is developed in Python and uses:

- **Python** — application logic.
- **pystray** — system tray icon and menu management.
- **Pillow** — icon loading.
- **Windows API (`ctypes`)** — power management requests to keep the system awake.

## 🚀 Getting started

### Option 1 — Windows executable

If a release containing `KeepMeOn.exe` is available:

1. Download the executable from the [Releases](../../releases) section.
2. Run `KeepMeOn.exe`.
3. Find the KeepMeOn icon in the Windows system tray.
4. Use **Keep PC awake** to enable or disable the feature.
5. Select **Exit** to close the application and restore normal power behavior.

*No need to keep a window open: KeepMeOn quietly runs in the background.*

### Option 2 — Run from source

If you prefer to run the project directly with Python:

**1. Clone the repository**

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

**2. Install the dependencies**

```bash
python -m pip install pystray pillow
```

**3. Run the application**

```bash
python main.py
```

Make sure to preserve the project's expected folder structure and include the required `icon.png` file.

## ⚙️ How does it work?

KeepMeOn uses the Windows API to tell the operating system that it should remain awake.

When enabled, the application requests that Windows prevent automatic system and display sleep. When the feature is disabled or the application exits, the request is cleared.

**Note:** KeepMeOn does not prevent manual shutdown, replace Windows power settings, prevent battery drain, or protect against shutdowns caused by other issues.

## 🧑‍💻 Why this project?

KeepMeOn started with a simple idea: build a small, practical utility that solves a common problem.

No unnecessary features. No endless configuration. Just what you need, when you need it.

## 🆓 Free and open source

KeepMeOn is available free of charge.

You can explore the source code, try the application, and report problems through the [Issues](../../issues) section.

> **License note:** Free of charge does not automatically mean open source. An explicit license must be added to the repository to define the rights to use, modify, and redistribute the code.

## 🐛 Issues and suggestions

Found a bug or have an idea to improve KeepMeOn?

Open an [Issue](../../issues) on GitHub and describe the problem or feature you would like to see implemented.

Every suggestion can help make the project better!

---

<div align="center">

**KeepMeOn — Stay awake. Stay productive. ☕**

*Made with Python for people who prefer a PC that doesn't fall asleep on the job.*

</div>
