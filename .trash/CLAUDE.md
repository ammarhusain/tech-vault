# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian-based personal knowledge management system ("second brain") with:
- Daily journaling (3-Daily/)
- Project tracking (1-Projects/)
- Long-term focus areas (2-Focus-Areas/)
- Archive system (4-Archive/)
- AI/ML research notes (ai-ml/)

## Automation and Commands

### Git Backup
The vault has automated daily git backups configured via LaunchAgent:
- Runs daily at 8:05 AM (even if computer was asleep)
- LaunchAgent config: `vault-management/com.obsidian.vault-git-backup.plist`
- Note: The referenced backup script is at a different path than the current vault location

### Vault Management Scripts
Python utilities in `vault-management/vault-manage.ipynb`:
- `get_files_to_index()` - Find files with specific tags (e.g., 'publish: true')
- `replace_line_in_file()` - Bulk string replacements
- `remove_line_in_file()` - Remove specific lines from files
- `replace_string_in_files()` - Directory-wide string replacements

## Key Obsidian Features Used

### Task Management
Uses Obsidian Tasks plugin with queries like:
```
```tasks
not done
(tags include #todo) AND (path includes apple)
```
```

Key task tags:
- `#todo` - Personal tasks
- `#j595/todo` - Work-related tasks  
- `#goal` - Goals
- `#goal_long_term` - Long-term goals

### DataView Queries
Extensive use for dynamic content aggregation:
- Task lists grouped by tags
- Recent notes by creation/modification date
- Cross-references between notes
- Content extraction from daily notes

### Command Center Dashboard
`command-center.md` serves as the main dashboard with:
- Aggregated task views (work vs personal)
- Goals tracking
- Recent notes
- Meditations log

## Directory Structure Notes

- **3-Daily/**: Daily journal entries organized by year
- **attachments/**: Binary files (PDFs, images, etc.) organized by context
- **ai-ml/**: Machine learning research with "*shiny-fm-*" prefixed files for different ML domains
- **vault-management/**: Automation scripts and vault maintenance tools

## Important Considerations

1. This vault contains personal and potentially sensitive information
2. Daily notes follow the pattern: `YYYY-MM-DD-DayName.md`
3. The vault is actively maintained with git commits
4. Files prefixed with "*" appear to be important reference documents
5. Heavy use of tags for organization and filtering