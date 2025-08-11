{
  description = "Reveal.js presentation development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            nodejs_20
            nodePackages.npm
            nodePackages.live-server
          ];

          shellHook = ''
            echo "Reveal.js development environment loaded"
            echo "Run 'npm install' to install dependencies"
            echo "Run 'live-server' to start development server"
          '';
        };
      });
}

