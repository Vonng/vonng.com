HUGO ?= hugo
OINK_LOCAL ?= $(HOME)/pgsty/oink
PORT ?= 1313

# Keep local development independent of module workspaces and vendored pins.
export GOWORK := off
export HUGO_MODULE_WORKSPACE := off
PINNED_HUGO = env -u HUGO_MODULE_REPLACEMENTS $(HUGO)
LOCAL_HUGO = HUGO_MODULE_REPLACEMENTS="github.com/pgsty/oink -> $(abspath $(OINK_LOCAL))" $(HUGO) --ignoreVendorPaths=github.com/pgsty/oink

default: dev

d:dev
dev: theme-local
	$(LOCAL_HUGO) server --renderToMemory -DFE --bind 127.0.0.1 --port "$(PORT)" --noBuildLock

b:build
build:
	$(PINNED_HUGO) --gc --minify --cleanDestinationDir --baseURL "https://vonng.com/"

c: check
check:
	$(PINNED_HUGO) --gc --printPathWarnings --panicOnWarning

# The build already reads the live numbers; this only refreshes the fallback
# checked into data/metrics.yaml. It edits a tracked file, so it is a
# deliberate step rather than something any other target runs for you.
m: metrics
metrics:
	python3 bin/update-metrics.py --write

# Retired 2026-09-18: the jp host is decommissioned. The site now publishes
# from git — a push to main builds vonng.com on Cloudflare Pages and
# blog.vonng.com through .github/workflows/pages.yaml. Kept for reference in
# case a host-based mirror is ever wanted again.
#
# s: sync
# sync: build
#	@! rg -q '(<link>|href="?|content="?)https?://(localhost|127\.0\.0\.1):[0-9]+' \
#		public --glob '*.html' --glob '*.xml'
#	rsync -avz public/ jp:/data/web/vonng.com/

.PHONY: default d dev b build c check m metrics

# Fail explicitly if a local theme was requested but is unavailable.
theme-local:
	@test -f "$(OINK_LOCAL)/hugo.yaml" || { echo "Set OINK_LOCAL to an OINK checkout (default: ~/pgsty/oink)." >&2; exit 1; }

.PHONY: theme-local
