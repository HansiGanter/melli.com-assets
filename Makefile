TEAM_DIR=team
TEAM_JPGS=$(wildcard $(TEAM_DIR)/*.jpg)
DEST_TEAMS_WEB=$(patsubst $(TEAM_DIR)/%.jpg, public/$(TEAM_DIR)/%.webp, $(TEAM_JPGS))

JOBS_DIR=jobs
JOBS_JPGS=$(wildcard $(JOBS_DIR)/*.jpg)
DEST_JOBS_WEB=$(patsubst $(JOBS_DIR)/%.jpg, public/$(JOBS_DIR)/%.webp, $(JOBS_JPGS))

STOCK_DIR=stock
STOCK_JPGS=$(wildcard $(STOCK_DIR)/*.jpg)
DEST_STOCK_WEB=$(patsubst $(STOCK_DIR)/%.jpg, public/$(STOCK_DIR)/%.webp, $(STOCK_JPGS))

all: $(DEST_TEAMS_WEB) $(DEST_JOBS_WEB) $(DEST_STOCK_WEB)

public/team/%.webp: team/%.jpg
	cwebp -resize 0 512 -o $@ $<

public/jobs/%.webp: jobs/%.jpg
	cwebp -resize 0 1024 -o $@ $<

public/stock/%.webp: stock/%.jpg
	cwebp -resize 0 1024 -o $@ $<
