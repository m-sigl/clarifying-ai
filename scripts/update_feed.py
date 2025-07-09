import os
import json
from datetime import datetime

signals_dir = "signals-left-on"
output_file = "system/feed.json"

signals = []

for filename in sorted(os.listdir(signals_dir)):
    if filename.endswith(".html"):
        path = f"{signals_dir}/{filename}"
        title = filename.replace("-", " ").replace(".html", "").title()
        updated = datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
        signals.append({
            "title": title,
            "url": f"/{path}",
            "updated": updated
        })

with open(output_file, "w") as f:
    json.dump(signals, f, indent=2)

print(f"Wrote {len(signals)} signals to {output_file}")
