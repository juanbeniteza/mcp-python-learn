# Python MCP Server - User Guide

This guide explains how you can ask Cline (the AI assistant) to use the tools and resources provided by the locally running Python MCP server. This server helps manage files within the `files` directory of this project.

## How to Interact with Cline

You can instruct Cline to use the server's capabilities by making specific requests in plain language. Here are examples based on the available tools and resources:

### Creating Files

The server has a `create_file` tool. To use it, you can ask Cline:

- "Cline, create a new file named `my_notes.txt` in the `files` directory with the content 'These are my notes'."
- "Can you use the Python server to make a file called `data.csv` containing 'header1,header2'?"

Cline will then use the `create_file` tool on your behalf.

### Accessing File Content

The server provides a resource template `files://local/{filename}` to read file contents. To use this, ask Cline:

- "Cline, what is the content of `file1.txt` in the `files` directory?"
- "Can you show me what's inside `my_notes.txt` using the Python server?"

Cline will access the resource `files://local/file1.txt` (or the specified filename) to retrieve the content for you.

### Listing Files

The server has a direct resource `files://local` to list files in the `files` directory. Ask Cline:

- "Cline, list all the files available through the Python server's `files` directory."
- "What files are currently managed by the Python MCP server?"

Cline will access the `files://local` resource to get the list.

## Summary of Server Capabilities

- **Tool:** `create_file(filename, content)` - Creates a file in the `files` directory.
- **Resource:** `files://local/{filename}` - Reads the content of a specific file in the `files` directory.
- **Resource:** `files://local` - Lists all files in the `files` directory.

Just tell Cline what you need to do with the files in the `files` directory, and it can leverage this server to help!
