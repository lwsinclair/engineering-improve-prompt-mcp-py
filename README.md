# Engineer Improve Prompt MCP Server

An MCP (Model Context Protocol) server that helps improve engineering prompts by making them clearer, more specific, and more actionable.

## Prerequisites

- Python 3.11 or higher
- Claude Desktop app

## Installation

### Step 1: Install uv (Python package manager)

First, install `uv` if you haven't already:

**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal or run:
```bash
source ~/.bashrc  # or ~/.zshrc on macOS
```

### Step 2: Install uvx

`uvx` comes bundled with `uv`, so once you have `uv` installed, `uvx` is automatically available.

Verify the installation:
```bash
uvx --version
```

### Step 3: Clone or Download this Repository

```bash
git clone <repository-url>
cd engineering-improve-prompt-mcp-py
```

Or download and extract the ZIP file from GitHub.

### Step 4: Install Dependencies

In the project directory, run:
```bash
uv sync
```

This will create a virtual environment and install all required dependencies.

## Testing the Server

To test if the server works correctly:

```bash
uv run python engineer-imporove-prompt.py
```

You should see no errors. Press `Ctrl+C` to stop.

## Configuring Claude Desktop

### Step 1: Locate Claude Desktop Configuration

The configuration file is located at:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Step 2: Edit Configuration

Open the configuration file in a text editor. If it doesn't exist, create it.

Add the following configuration:

```json
{
  "mcpServers": {
    "engineer-improve-prompt": {
      "command": "uvx",
      "args": [
        "--from",
        "file:///absolute/path/to/engineering-improve-prompt-mcp-py",
        "mcp"
      ]
    }
  }
}
```

**Important**: Replace `/absolute/path/to/engineering-improve-prompt-mcp-py` with the actual absolute path to your project directory.

For example:
- **macOS**: `"file:///Users/yourusername/projects/engineering-improve-prompt-mcp-py"`
- **Windows**: `"file:///C:/Users/yourusername/projects/engineering-improve-prompt-mcp-py"`

### Alternative Configuration (Direct Python)

If the above doesn't work, you can use this alternative configuration:

```json
{
  "mcpServers": {
    "engineer-improve-prompt": {
      "command": "/absolute/path/to/engineering-improve-prompt-mcp-py/.venv/bin/python",
      "args": [
        "/absolute/path/to/engineering-improve-prompt-mcp-py/engineer-imporove-prompt.py"
      ]
    }
  }
}
```

### Step 3: Restart Claude Desktop

1. Completely quit Claude Desktop (not just close the window)
2. Start Claude Desktop again
3. Look for the MCP icon in Claude's interface to verify the server is connected

## Usage

Once configured, you can use the prompt improvement feature in Claude Desktop:

1. Open Claude Desktop
2. Look for the MCP servers icon (usually in the bottom or side panel)
3. You should see "engineer-improve-prompt" in the list
4. Click on it to see available prompts
5. Use the "Improve the prompt for an engineering task" function

The server will analyze your prompt and suggest improvements to make it:
- More specific and actionable
- Include necessary technical details
- Follow best practices for engineering tasks

## Troubleshooting

### Server not showing in Claude Desktop

1. Check the configuration file syntax (must be valid JSON)
2. Ensure all paths are absolute paths
3. Check Claude Desktop logs:
   - **macOS**: `~/Library/Logs/Claude/`
   - **Windows**: `%APPDATA%\Claude\logs\`

### Module not found errors

If you see `ModuleNotFoundError: No module named 'mcp'`:

1. Ensure you ran `uv sync` in the project directory
2. Verify the virtual environment exists: `ls .venv/`
3. Try running directly: `uv run python engineer-imporove-prompt.py`

### Permission errors

On macOS/Linux, ensure the script is executable:
```bash
chmod +x engineer-imporove-prompt.py
```

## Development

To modify the prompt improvement logic, edit `engineer-imporove-prompt.py`.

To test changes:
```bash
# Run the development server with inspector
uv run python .venv/bin/mcp dev engineer-imporove-prompt.py
```

This will start a development server with a web-based inspector at `http://localhost:6274`.

## License

[Your License Here]

## Contributing

[Your Contributing Guidelines Here]