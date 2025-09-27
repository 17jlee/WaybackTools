# WaybackTools

A collection of Python utilities for recovering website data from the Wayback Machine following a cyber attack and data loss.

## Background

These tools were created to help recover archived website content after our school suffered a cyber attack that resulted in significant data loss. 

The scripts automate the process of downloading and orgainising archived pages from the Internet Archive's Wayback Machine.

## Tools

### Batch Downloader.py
Downloads all Wayback Machine URLs listed in a text file using the `wayback_machine_downloader` tool.

**Usage:**
```bash
python "Batch Downloader.py" path/to/wayback_links.txt
```

### Tab Formatting.py
Cleans up URL lists by removing query parameters (everything after `?`) to create cleaner archive links.

**Usage:**
```bash
python "Tab Formatting.py" input_file.txt output_file.txt
```

### Formatting.py
Renames downloaded files to match their original URLs, handling URL encoding issues in filenames.

**Usage:**
```bash
python "Formatting.py" raw_links.txt edited_links.txt
```

## Prerequisites

- Python 3.x
- [wayback_machine_downloader](https://github.com/hartator/wayback-machine-downloader) gem

## Workflow

1. Collect Wayback Machine URLs for your site
2. Clean URLs with `Tab Formatting.py`
3. Download archives with `Batch Downloader.py`
4. Rename files with `Formatting.py`

## Note

These tools were developed for emergency data recovery purposes. While functional, they may require modification for different use cases.
