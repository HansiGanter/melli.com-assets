# Assets

::: error
To the engineers: DO NOT PUT ANY SECRETS INTO THIS FOLDER. This repository is mirrored to Nextcloud. Even if a file is git-ignored, it still will be synced to Nextcloud.

:::

::: info
To normal people: This folder is synced with our GitHub. Put the high-quality image files into the `images` folder. Then tell a engineer to create the compressed versions and push them to our CDN.

:::

## TODO

* Fix the `images/images` duplication and add the `hansi`\-redirect: Make `assets.melli.com/images/images` point to `assets.melli.com/images`

## Workflow

* Every file in the `public` folder will be deployed under `https://assets.melli.com` when a commit is pushed to [GitHub's ](https://github.com/melli-labs/assets)`main` branch.

## Folder Overview

All files in `/images` will be compressed in to WebP to improve performance. We compress them to a resolution of 512x?? WebP files which are approximately 15 kB. Images which are larger than 512px will also be compressed into 1024x?? and prefixed with `...-1024.webp`.

Files that don't require a build step are directly stored in the `/public` folder.

| Folder | Build Step | Description |
|:-------|:-----------|-------------|
| `/public` | none | Will be deployed |
| `/images` | compressed to WebP | Original images |

## Build Instructions

### Setup

The `flake.nix` provides a development environment with:

* `cwebp`
* `doit` - A Python task runner
* `Python + deps`

Activate development environment:

```sh
nix develop
# or install direnv to automatically activate env
direnv allow
```

### Build

Run all build steps:

```sh
doit
```

Run a specific build step:

```sh
doit run -s webp:public/images/team/benjamin-mollier.webp
# or
doit run -s webp:public/images/team/benjamin-mollier-1024.webp
```