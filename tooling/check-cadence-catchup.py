#!/usr/bin/env python3
"""Check whether today's publication is complete or if an immediate catch-up is required."""
import json
from pathlib import Path
from datetime import datetime
import zoneinfo

ROOT = Path(__file__).resolve().parents[1]
state = json.loads((ROOT / 'publishing/run-state.json').read_text())
queue = json.loads((ROOT / 'publishing/book-queue.json').read_text())

tz = zoneinfo.ZoneInfo(state.get('timezone', 'Asia/Dhaka'))
now = datetime.now(tz)
today_str = now.strftime('%Y-%m-%d')
last_pub = state.get('last_successful_publication_date')

is_published_today = (last_pub == today_str)
next_book = state.get('next_book_id')

status = {
    'current_time': now.isoformat(),
    'timezone': state.get('timezone'),
    'today_local_date': today_str,
    'last_successful_publication_date': last_pub,
    'is_published_today': is_published_today,
    'next_book_in_queue': next_book,
    'catchup_policy_active': state.get('catchup_policy', {}).get('enabled', False)
}

if is_published_today:
    status['action_required'] = 'none_completed_for_today'
    status['message'] = f"Today's book ({state.get('last_published_book_id')}) is already published for {today_str}. Next scheduled run: tomorrow at 12:00 PM."
elif now.hour >= 12:
    status['action_required'] = 'immediate_catchup_required'
    status['message'] = f"12:00 PM has passed for {today_str} and no book was published yet. Immediate catch-up required for {next_book}."
else:
    status['action_required'] = 'waiting_for_noon'
    status['message'] = f"Scheduled for 12:00 PM on {today_str} for {next_book}."

print(json.dumps(status, indent=2))
