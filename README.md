# Assets

## Workflow

* Every file in the `public` folder will be deployed under `https://assets.melli.com` when a commit is pushed to [GitHub's `main` branch](https://gitlab.com/mit-emilia/assets).
* If you're viewing this folder from internal cloud `OCA/meetap/assets` and don't know/care what a Git commit is, then just add your file and ask one of our developers to handle the rest.

## Folder Overview

Some files require a build step to improve the loading performance. For example, our team photos stored at `/team` are about 1 MB in size. We compress them to 512x512 WebP files which are approximately 15 kB. Files that don't require a build step are directly stored in the `/public` folder.

| Folder                  | Build Step              | Description                     |
| :---------------------- | :---------------------- | ------------------------------- |
| `/stock`                | compressed to 1024 WebP | Stock photos for website        |
| `/jobs`                 | compressed to 1024 WebP | Stock photos for job posting    |
| `/team`                 | compressed to 512 WebP  | Photos of our team              |
| `/public/<filename>`    | none                    | e.g. favicon.svg or logo.svg    |
| `/public/shapes`        | none                    | masks for images                |
| `/public/icons`         | none                    | e.g. placeholder avatar         |
| `/public/illustrations` | none                    | Illustrations                   |

## Build Instructions

### Setup

The `flake.nix` provides a development environment with:

* `GNU make`
* `cwebp`

Activate development environment:

```sh
nix develop
# or install direnv to automatically activate env
direnv allow
```

### Build

Run all build steps:

```sh
make
```

Run a specific build step:

```sh
make public/team
```

Or, run for a single file:

```sh
make public/team/hans-ganter.webp
```
