TEAM_DIR=team
TEAM_JPGS=$(wildcard $(TEAM_DIR)/*.jpg)

DEST_TEAMS_WEB=$(patsubst $(TEAM_DIR)/%.jpg, public/$(TEAM_DIR)/%.webp,$(TEAM_JPGS))

all: $(DEST_TEAMS_WEB)

public/team/%.webp: team/%.jpg
	cwebp -resize 0 512 -o $@ $<
