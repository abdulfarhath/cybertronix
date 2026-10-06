#!/bin/bash
# Every new session on this repo: point Claude at the hub memory, so the founder can just say "continue".
# (stdout from a SessionStart hook is added to Claude's context.)
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git pull -q --ff-only 2>/dev/null || true
cat <<'MSG'
Cybertronix repo. If the founder is talking to you, you are the HUB: before your first reply read
docs/memory/README.md and docs/memory/founder-messages.md, then docs/HANDOVER.md. Never ask the founder for context.
A bare "continue" or "hi" means: do docs/memory/README.md section 7 (send key screenshots from design/previews/ as images).
MSG
exit 0
