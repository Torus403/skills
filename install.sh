#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
manifest=".jack-skills"

install_into() {
  local dest="$1"
  mkdir -p "$dest"
  if [ -f "$dest/$manifest" ]; then
    while IFS= read -r name; do
      [ -n "$name" ] && rm -rf "${dest:?}/$name"
    done < "$dest/$manifest"
  fi
  : > "$dest/$manifest"
  for src in "$repo"/skills/*/; do
    name="$(basename "$src")"
    rm -rf "${dest:?}/$name"
    cp -R "$src" "$dest/$name"
    echo "$name" >> "$dest/$manifest"
  done
  echo "Installed $(wc -l < "$dest/$manifest" | tr -d ' ') skills into $dest"
}

install_into "$HOME/.claude/skills"
install_into "$HOME/.agents/skills"

mkdir -p "$HOME/.claude/agents"
cp "$repo"/agents/*.md "$HOME/.claude/agents/"
echo "Installed $(ls "$repo"/agents/*.md | wc -l | tr -d ' ') subagents into $HOME/.claude/agents"
