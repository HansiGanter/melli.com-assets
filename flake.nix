{
  description = "Emilia Assets";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (
      system: with nixpkgs.legacyPackages.${system};
      {
        devShell = mkShell {
          nativeBuildInputs = [ bashInteractive ];
          buildInputs = [
            libwebp
            (python39.withPackages (p: with p; [ doit black ]))
          ];
        };
      }
    );
}
