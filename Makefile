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
# checked into data/metrics.yaml, so it is a deliberate step, not part of sync.
m: metrics
metrics:
	python3 bin/update-metrics.py --write

s: sync
sync: build
	@! rg -q '(<link>|href="?|content="?)https?://(localhost|127\.0\.0\.1):[0-9]+' \
		public --glob '*.html' --glob '*.xml'
	rsync -avz public/ jp:/data/web/vonng.com/

.PHONY: default d dev b build c check m metrics s sync
