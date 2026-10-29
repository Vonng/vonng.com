#!/usr/bin/env bash
# Run from any directory with ImageMagick 7 installed:
#   bash static/favicons/gen.sh
# The navbar's SVG is the source for both current and legacy icon URLs.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
source_svg="$repo_root/assets/img/vonng-logo.svg"
static_dir="$repo_root/static"
legacy_dir="$static_dir/favicons"

command -v magick >/dev/null || { echo 'ImageMagick 7 (magick) is required.' >&2; exit 1; }
icon_tmp="$(mktemp -d "${TMPDIR:-/tmp}/vonng-favicons.XXXXXX")"
trap 'rm -rf "$icon_tmp"' EXIT

# Supersample the vector before resizing so the 16px/32px edges stay smooth.
# Keep intermediate images outside the repository and strip PNG timestamps.
magick -background none -density 6144 "$source_svg" -strip "$icon_tmp/master.png"
render() {
  magick "$icon_tmp/master.png" -filter Lanczos -resize "${1}x${1}" \
    -depth 8 -strip "$2"
}

cp "$source_svg" "$static_dir/favicon.svg"
for size in 16 32 256 512; do
  render "$size" "$static_dir/favicon-${size}x${size}.png"
done
render 48 "$icon_tmp/favicon-48.png"
magick "$static_dir/favicon-16x16.png" "$static_dir/favicon-32x32.png" \
  "$icon_tmp/favicon-48.png" -strip "$static_dir/favicon.ico"

# iOS adds its own rounded corners; give the mark an opaque canvas and padding.
render 144 "$icon_tmp/touch.png"
magick "$icon_tmp/touch.png" -background '#f7f6f3' -alpha remove -alpha off \
  -gravity center -extent 180x180 -depth 8 -strip "$static_dir/apple-touch-icon.png"
cp "$static_dir/apple-touch-icon.png" "$static_dir/apple-touch-icon-180x180.png"
cp "$static_dir/apple-touch-icon.png" "$legacy_dir/apple-touch-icon-180x180.png"

# Preserve old URLs while making every exported variant use the same mark.
for size in 36 48 72 96 144 192; do
  render "$size" "$legacy_dir/android-${size}x${size}.png"
done
for size in 16 32; do
  cp "$static_dir/favicon-${size}x${size}.png" "$legacy_dir/favicon-${size}x${size}.png"
done
cp "$static_dir/favicon-256x256.png" "$legacy_dir/favicon-256.png"
render 1024 "$legacy_dir/favicon-1024.png"
cp "$legacy_dir/favicon-1024.png" "$legacy_dir/logo.png"
for size in 192 512; do
  render "$size" "$legacy_dir/pwa-${size}x${size}.png"
done
for size in 70 150 310; do
  render "$size" "$legacy_dir/tile${size}x${size}.png"
done
magick "$legacy_dir/tile150x150.png" -background none -gravity center \
  -extent 310x150 -depth 8 -strip "$legacy_dir/tile310x150.png"
