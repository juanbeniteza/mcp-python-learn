import os

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create an MCP server
mcp = FastMCP("Files")


# Add a tool to create a file
@mcp.tool()
def create_file(filename: str, content: str) -> str:
    """Create a file with the given filename and content"""
    file_path = os.path.join("files", filename)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File '{filename}' created successfully."
    except Exception as e:
        return f"Error creating file '{filename}': {e}"


# Add a resource to list all files
@mcp.resource("files://local")
def list_files() -> list[str]:
    """List files in the local directory"""
    files_dir = "files"
    try:
        # List all entries in the directory
        entries = os.listdir(files_dir)
        # Filter out directories, keeping only files
        files = [f for f in entries if os.path.isfile(os.path.join(files_dir, f))]
        return files
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error listing files: {e}")
        return []


# Add a resource to get file content
@mcp.resource("files://local/{filename}")
def get_file_content(filename: str) -> str:
    """Get the content of a specific file in the files directory"""
    file_path = os.path.join("files", filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except Exception as e:
        return f"Error reading file '{filename}': {e}"


# Add a prompt to summarize file content
@mcp.prompt()
def summarize_file(filename: str) -> str:
    """Generates a prompt to summarize the content of a given file."""
    content = get_file_content(filename)
    if content.startswith("Error:"):
        return [base.UserMessage(f"Could not summarize file: {content}")]

    return f"You are an expert summarizer. Provide a concise summary of the following text: {content}"


if __name__ == "__main__":
    mcp.run()
