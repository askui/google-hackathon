# 🧪 Google Hackathon with AskUI

Join us as we explore how to build your first AI-powered agent for automating software testing. With AskUI, you'll create agents that interact with interfaces visually—just like a human. No matter your experience level, this is your chance to experiment, learn, and build something innovative.

## ⚙️ Prerequisites

Before you can set up and run your agent, ensure you have the following installed:

- 🔄 [AskUI Shell](https://docs.askui.com) - The command line tool for AskUI Agents.
- 🖊️ A code editor of your choice (e.g., VSCode, PyCharm).
- 🔑 An Anthropic API key - Required for the VisionAgent to function properly.

## 🔧 Setup


### 1. Install AskUI Agent OS

Agent OS is a device controller that allows agents to take screenshots, move the mouse, click, and type on the keyboard across any operating system.

<details>
  <summary>Windows</summary>
  
  ##### AMD64

[AskUI Installer for AMD64](https://files.askui.com/releases/Installer/Latest/AskUI-Suite-Latest-User-Installer-Win-AMD64-Web.exe)

##### ARM64

[AskUI Installer for ARM64](https://files.askui.com/releases/Installer/Latest/AskUI-Suite-Latest-User-Installer-Win-ARM64-Web.exe)
</details>


<details>
  <summary>Linux</summary>

  **⚠️ Warning:** Agent OS currently does not work on Wayland. Switch to XOrg to use it.
  
##### AMD64

```shell
curl -L -o /tmp/AskUI-Suite-Latest-User-Installer-Linux-AMD64-Web.run https://files.askui.com/releases/Installer/Latest/AskUI-Suite-Latest-User-Installer-Linux-AMD64-Web.run
```
```shell
bash /tmp/AskUI-Suite-Latest-User-Installer-Linux-AMD64-Web.run
```

##### ARM64


```shell
curl -L -o /tmp/AskUI-Suite-Latest-User-Installer-Linux-ARM64-Web.run https://files.askui.com/releases/Installer/Latest/AskUI-Suite-Latest-User-Installer-Linux-ARM64-Web.run
```
```shell
bash /tmp/AskUI-Suite-Latest-User-Installer-Linux-ARM64-Web.run
```
</details>


<details>
  <summary>MacOS</summary>
  
```shell
curl -L -o /tmp/AskUI-Suite-Latest-User-Installer-MacOS-ARM64-Web.run https://files.askui.com/releases/Installer/Latest/AskUI-Suite-Latest-User-Installer-MacOS-ARM64-Web.run
```
```shell
bash /tmp/AskUI-Suite-Latest-User-Installer-MacOS-ARM64-Web.run
```
</details>


### 2. Install vision-agent in your Python environment

```shell
pip install askui
```

**Note:** Requires Python version >=3.10.

### 3a. Authenticate with an **AI Model** Provider

|  | AskUI [INFO](https://hub.askui.com/) | Anthropic [INFO](https://console.anthropic.com/settings/keys) |
|----------|----------|----------|
| ENV Variables    | `ASKUI_WORKSPACE_ID`, `ASKUI_TOKEN`   | `ANTHROPIC_API_KEY`   |
| Supported Commands    | `click()`, `get()`, `locate()`, `mouse_move()`   | `act()`, `click()`, `get()`, `locate()`, `mouse_move()`  |
| Description    | Faster Inference, European Server, Enterprise Ready   | Supports complex actions   |

To get started, set the environment variables required to authenticate with your chosen model provider.

#### How to set an environment variable?
1. Create `.env` file similar to `.env.template` and update required credentials.

### 3b. Test with 🤗 Hugging Face **AI Models** (Spaces API)

You can test the Vision Agent with Huggingface models via their Spaces API. Please note that the API is rate-limited so for production use cases, it is recommended to choose step 3a.

**Note:** Hugging Face Spaces host model demos provided by individuals not associated with Hugging Face or AskUI. Don't use these models on screens with sensible information.

**Supported Models:**
- [`AskUI/PTA-1`](https://huggingface.co/spaces/AskUI/PTA-1)
- [`OS-Copilot/OS-Atlas-Base-7B`](https://huggingface.co/spaces/maxiw/OS-ATLAS)
- [`showlab/ShowUI-2B`](https://huggingface.co/spaces/showlab/ShowUI)
- [`Qwen/Qwen2-VL-2B-Instruct`](https://huggingface.co/spaces/maxiw/Qwen2-VL-Detection)
- [`Qwen/Qwen2-VL-7B-Instruct`](https://huggingface.co/spaces/maxiw/Qwen2-VL-Detection)

**Example Code:**
```python
agent.click("search field", model="OS-Copilot/OS-Atlas-Base-7B")
```

### 3c. Host your own **AI Models**

#### UI-TARS

You can use Vision Agent with UI-TARS if you provide your own UI-TARS API endpoint.

1. Step: Host the model locally or in the cloud. More information about hosting UI-TARS can be found [here](https://github.com/bytedance/UI-TARS?tab=readme-ov-file#deployment).

2. Step: Provide the `TARS_URL` and `TARS_API_KEY` environment variables to Vision Agent.

3. Step: Use the `model="tars"` parameter in your `click()`, `get()` and `act()` etc. commands or when initializing the `VisionAgent`.



## ▶️ Run Your Agent

This agent runs automated UI tests using Pytest and AskUI's VisionAgent. When run, it:

1. Initializes the VisionAgent
2. Executes test cases defined in the `tests/` directory
3. Performs UI interactions like clicks and assertions
4. Reports test results

To run your agent locally:

```sh
pytest --verbose
```

�� Happy Coding! 🚀
