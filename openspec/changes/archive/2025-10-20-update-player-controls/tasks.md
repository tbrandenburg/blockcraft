## 1. Implementation
- [x] 1.1 Update UI input capture to include keyboard states and mouse look delta
- [x] 1.2 Apply movement in the game manager using captured input and ensure physics keeps player grounded
- [x] 1.3 Add camera controller tying player position to view direction with mouse look
- [x] 1.4 Verify WASD movement and mouse look work in-game via manual run
- [x] 1.5 Add automated coverage for input handling and player movement updates

## 2. Validation
- [x] 2.1 Run `uv run pytest`
- [x] 2.2 Run `uv run openspec validate update-player-controls --strict`
