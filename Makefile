default: dev

d:dev
dev:
	HUGO_MODULE_REPLACEMENTS='github.com/pgsty/oink -> $(HOME)/pgsty/oink' hugo server --renderToMemory -DFE

b:build
build:
	hugo --gc --minify --cleanDestinationDir --baseURL "https://vonng.com/"

c: check
check:
	hugo --gc --printPathWarnings --panicOnWarning

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
