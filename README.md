# Assets

## Workflow

* Every file in the `public` folder will be deployed under `https://assets.melli.com` when a commit is pushed to [GitHub's `main` branch](https://github.com/melli-labs/assets).
* If you're viewing this folder from internal cloud `OCA/meetap/assets` and don't know/care what a Git commit is, then just add your file and ask one of our developers to handle the rest.

## Folder Overview

All files in `/images` will be compressed in to WebP to improve performance. We compress them to a resolution of 512x?? WebP files which are approximately 15 kB. Images which are larger than 512px will also be compressed into 1024x?? and prefixed with `...-1024.webp`.

Files that don't require a build step are directly stored in the `/public` folder.

| Folder                  | Build Step              | Description                     |
| :---------------------- | :---------------------- | ------------------------------- |
| `/public`               | none                    | Will be deployed                |
| `/images`               | compressed to WebP      | Original images                 |

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
