all: public/stock public/team public/jobs

# Stock Photos
STOCK_DIR=stock
STOCK_JPGS=$(wildcard $(STOCK_DIR)/*.jpg)
DEST_STOCK_WEB=$(patsubst $(STOCK_DIR)/%.jpg, public/$(STOCK_DIR)/%.webp, $(STOCK_JPGS))

public/stock: $(DEST_STOCK_WEB)

public/stock/%.webp: stock/%.jpg
	cwebp -resize 0 1024 -o $@ $<

# Team Photos
TEAM_DIR=team
TEAM_JPGS=$(wildcard $(TEAM_DIR)/*.jpg)
DEST_TEAMS_WEB=$(patsubst $(TEAM_DIR)/%.jpg, public/$(TEAM_DIR)/%.webp, $(TEAM_JPGS))

public/team: $(DEST_TEAMS_WEB)

public/team/%.webp: team/%.jpg
	cwebp -resize 0 512 -o $@ $<

# Job Posting Photos
JOBS_DIR=jobs
JOBS_JPGS=$(wildcard $(JOBS_DIR)/*.jpg)
DEST_JOBS_WEB=$(patsubst $(JOBS_DIR)/%.jpg, public/$(JOBS_DIR)/%.webp, $(JOBS_JPGS))

public/jobs: $(DEST_JOBS_WEB)

public/jobs/%.webp: jobs/%.jpg
	cwebp -resize 0 1024 -o $@ $<
