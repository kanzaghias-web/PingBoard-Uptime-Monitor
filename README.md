# PingBoard Uptime Monitor

PingBoard is a lightweight Python uptime monitor for checking a list of URLs and logging response times. It is meant to feel like small internal tooling: simple, scriptable, and easy to extend.

## What it does

- Sends HTTP requests to a list of target URLs
- Records response status and response time
- Prints or logs failures for quick review
- Serves as a base for scheduling, alerts, and configuration improvements

## Current status

This version supports a single run against a fixed set of targets. Scheduled checks, Slack alerts, and config-based targets are planned next.

## Example use case

Use PingBoard to quickly verify whether key internal or external endpoints are reachable and how long they take to respond.

## Project structure

```text
.
├── ping.py
└── README.md
```

## How to run

1. Install Python 3.10+.
2. Install dependencies if needed.
3. Run the script:

```bash
python ping.py
```

## Roadmap

- Add interval-based scheduling
- Send Slack alerts when checks fail
- Move monitored targets into a YAML config file
- Improve timeout and error handling
- Add better output and logging

## Notes

This repository is intentionally small and incremental. The goal is to show a believable evolution from a basic one-off checker into a more useful internal monitoring tool.
