{
  description = "A flake for Marp presentations.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell
          {
            buildInputs = with pkgs; [
              marp-cli
              nodejs
              chromium
            ];

            shellHook = ''
              echo "Marp dev environment loaded..."
            '';
          };
      });
}
