# Microsoft Graph Tool

Microsoft Graph integration for Outlook mail, Microsoft Teams messaging, and OneDrive file operations.

## Setup

```bash
# Required
export MICROSOFT_GRAPH_ACCESS_TOKEN=your-access-token
```

**Get your token:**
1. Register an Azure AD application in the [Azure Portal](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).
2. Grant delegated Microsoft Graph permissions for the operations you need (for example: `Mail.Read`, `Mail.Send`, `Team.ReadBasic.All`, `ChannelMessage.Send`, `Files.ReadWrite`).
3. Complete an OAuth flow to get an access token.
4. Set `MICROSOFT_GRAPH_ACCESS_TOKEN` in your environment.

Alternatively, configure credentials via Aden's credential store using the `microsoft_graph` key.

## Tools (8)

| Tool | Description |
|------|-------------|
| `outlook_list_messages` | List messages from an Outlook mail folder with optional unread/search filtering. |
| `outlook_get_message` | Fetch full details for a specific Outlook message. |
| `outlook_send_mail` | Send an Outlook email with optional CC and HTML body support. |
| `teams_list_teams` | List Teams the current user belongs to. |
| `teams_list_channels` | List channels for a Team. |
| `teams_send_channel_message` | Send a message to a Teams channel. |
| `onedrive_search_files` | Search OneDrive files by query string. |
| `onedrive_upload_file` | Upload text content as a file to OneDrive. |

## Usage

### List inbox messages

```python
result = outlook_list_messages(folder="inbox", max_results=10, filter_unread=True)
# Returns: {"folder": "inbox", "messages": [...]} 
```

### Send a Teams channel message

```python
result = teams_send_channel_message(
    team_id="<team-id>",
    channel_id="<channel-id>",
    message="Release is live.",
)
# Returns: {"status": "sent", "team_id": "...", "channel_id": "...", "messageId": "..."}
```

## Scope

- Outlook message listing, retrieval, and sending.
- Teams discovery and channel messaging.
- OneDrive search and simple text file uploads.

## API Reference

- [Microsoft Graph REST API Overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
